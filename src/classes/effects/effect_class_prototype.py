from __future__ import annotations
import src.classes.entity_prototype as ch
import src.classes.temp.temp_class_handler as tp
import uuid
from helpers import log, Log


class Effect:
    def __init__(self, typo, name, desc, turns, active, is_stackable,stacks, character,has_temp, temp_objs,temp_owner):
        self.uuid = uuid.uuid4()
        self.typo = typo
        self.name = name
        self.desc = desc
        self.turn = turns
        self.active = active
        self.is_stackable = is_stackable
        self.stacks = stacks
        self.has_temp = has_temp
        self.temp_objs: list[tp.Temp] = temp_objs
        self.temp_owner: ch.Character | ch.Attributes = temp_owner
        self.owner : ch.Character = character



    def process_effect(self):
        pass

    def end_effect(self):
        self.active = False
        log(Log.DEBUG,f"Effect {self.name} has ended", f"[{self.owner.name}][EffectHandler][Effect]")

        if self.has_temp:
            if isinstance(self.temp_owner,ch.Character) and self.temp_owner.attributes is not None and self.temp_owner.attributes.temp_handler is not None:
                self.temp_owner.attributes.temp_handler.remove_temp(list_temp=self.temp_objs)
            elif isinstance(self.temp_owner,ch.Attributes) and self.temp_owner.attributes.temp_handler is not None:
                self.temp_owner.temp_handler.remove_temp(list_temp=self.temp_objs)




class Burn(Effect):
    def __init__(self,typo,name,desc,turns,active,is_stackable,stacks,character, has_temp, temp_objs: list[tp.Temp] = None, temp_owner: ch.Character | ch.Attributes  = None):
        super().__init__(typo=typo,name=name,desc=desc,turns=turns,active=active,is_stackable=is_stackable,stacks=stacks,character=character,has_temp=has_temp, temp_objs=temp_objs, temp_owner=temp_owner)


    def process_effect(self):
        if self.turn > 0 and self.active:
            dmg = self.owner.attributes.status.hp * (0.1 * self.stacks)
            log(Log.MAIN, f"took {dmg} burn damage", f"[{self.owner.name}][Effect]")
            self.owner.attributes.status.hp -= dmg
            self.turn -= 1

            if self.turn <= 0:
                self.end_effect()
                return False

            return True