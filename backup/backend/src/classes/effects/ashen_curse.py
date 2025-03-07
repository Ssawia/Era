from __future__ import annotations
from src.classes.effects.effect_class import Effect
import src.classes.entity_prototype as ch
import src.classes.temps.temp_class_handler as tp
from src.classes.temps.temp_class_handler import Temp
from helpers import log, Log




class AshenCurse(Effect):
    def __init__(self,typo,name,desc,turns,active,is_stackable,stacks,max_stacks,character, has_temp, temp_objs: list[tp.Temp] = None, temp_owner: ch.Character | ch.Attributes  = None, giver = None):
        super().__init__(typo=typo,name=name,desc=desc,turns=turns,active=active,is_stackable=is_stackable,stacks=stacks,max_stacks=max_stacks,character=character,has_temp=has_temp, temp_objs=temp_objs, temp_owner=temp_owner, giver=giver)
                     


    def process_effect(self):
        if self.turn > 0 and self.active:
            dmg = 1 * self.stacks
            log(Log.INFO, f"took {dmg} burn damage", f"[Effect][{self.owner.name}][{self.name}][Stacks: {self.stacks}]")
            
            self.owner.attributes.status.hp -= dmg
            if self.owner.attributes.status.hp <= 0:
                self.owner.attributes.status.hp = 0

            self.turn -= 1

            if self.turn <= 0:
                self.end_effect()
                return False

            return True