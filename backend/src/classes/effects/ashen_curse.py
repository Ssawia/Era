from __future__ import annotations
from src.classes.effects.effect_class import Effect
import src.classes.entity.character as ch
import src.classes.temps.temp_class_handler as tp
from src.classes.temps.temp_class_handler import Temp
from helpers import log, Log
import random




class AshenCurse(Effect):
    def __init__(self,typo,name,desc,turns,active,is_stackable,stacks,max_stacks,giver,character, has_temp, temp_objs, obj_values, event):
        super().__init__(typo=typo,name=name,desc=desc,turns=turns,active=active,is_stackable=is_stackable,stacks=stacks,max_stacks=max_stacks,giver=giver,character=character,has_temp=has_temp, temp_objs=temp_objs, obj_values=obj_values, event=event)
                     


    def process_effect(self):
        if self.turn > 0 and self.active:
            ash_text = "ashen_curse_perc"
            ash_perc = self.obj_values[ash_text] + self.giver.attributes.temp_handler.get_add_bonus(ash_text, "add")
            dmg = 1 * self.stacks
            log(Log.INFO, f" took {dmg} burn damage", f"[Effect][{self.owner.name}][{self.name}][Stacks: {self.stacks}]")
            
            self.owner.attributes.status.hp -= dmg
            if self.owner.attributes.status.hp <= 0:
                self.owner.attributes.status.hp = 0
            self.turn -= 1

            roll = random.randint(1,100)

            if roll <= ash_perc:
                log(Log.INFO, f" {self.name} activated its second effect")


            if self.turn <= 0:
                self.end_effect()
                return False

            return True