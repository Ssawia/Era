from __future__ import annotations
import src.classes.entity_prototype as ch
import src.classes.temp.temp_class_handler as tp
import uuid
from helpers import log, Log
from math import trunc


class Effect:
    def __init__(self, typo, name, desc, turns, active, is_stackable,stacks, max_stacks, character,has_temp, temp_objs,temp_owner):
        self.uuid = uuid.uuid4()
        self.typo = typo
        self.name = name
        self.desc = desc
        self.turn = turns
        self.active = active
        self.is_stackable = is_stackable
        self.stacks = stacks
        self.max_stacks = max_stacks
        self.has_temp = has_temp
        self.temp_objs: list[tp.Temp] = temp_objs
        self.temp_owner: ch.Character | ch.Attributes = temp_owner
        self.owner : ch.Character = character
    

    def init_effect(self):
        pass


    def process_effect(self):
        pass

    def end_effect(self):
        self.active = False
        log(Log.INFO,f"Effect {self.name} has ended", f"[{self.owner.name}][EffectHandler][Effect]")

        if self.has_temp:
            if isinstance(self.temp_owner,ch.Character) and self.temp_owner.attributes is not None and self.temp_owner.attributes.temp_handler is not None:
                self.temp_owner.attributes.temp_handler.remove_temp(list_temp=self.temp_objs)
                self.temp_owner.attributes.temp_handler.update_temp()
            elif isinstance(self.temp_owner,ch.Attributes) and self.temp_owner.attributes.temp_handler is not None:
                self.temp_owner.temp_handler.remove_temp(list_temp=self.temp_objs)
                self.temp_owner.attributes.temp_handler.update_temp()




class AshenCurse(Effect):
    def __init__(self,typo,name,desc,turns,active,is_stackable,stacks,max_stacks,character, has_temp, temp_objs: list[tp.Temp] = None, temp_owner: ch.Character | ch.Attributes  = None):
        super().__init__(typo=typo,name=name,desc=desc,turns=turns,active=active,is_stackable=is_stackable,stacks=stacks,max_stacks=max_stacks,character=character,has_temp=has_temp, temp_objs=temp_objs, temp_owner=temp_owner)

        self.init_effect()
    
    def init_effect(self):
            if self.name not in self.owner.attributes.temp_handler.flags:
                log(Log.DEBUG, f"Debuff Fire Resistance add to {self.owner.name}", "[Temp]")
                self.has_temp = True
                self.temp_owner = self.owner
                temp = tp.Temp("Fire_Res","mult",1,0,-0.10,True,True,False,"Ashen Curse")
                self.temp_objs = [temp]
                self.owner.attributes.temp_handler.add_temp(self.temp_objs)
            else:
                log(Log.DEBUG, f"Debuff Fire is arealdy in  {self.owner.name}", "[Temp]")

    def process_effect(self):
        if self.turn > 0 and self.active:
            dmg = trunc(self.owner.attributes.status.hp * (0.05 * self.stacks))
            log(Log.INFO, f"took {dmg} burn damage", f"[{self.owner.name}][{self.name}][Effect]")


            
            self.owner.attributes.status.hp -= dmg
            if self.owner.attributes.status.hp <= 0:
                self.owner.attributes.status.hp = 0

            self.turn -= 1

            if self.turn <= 0:
                self.end_effect()
                return False

            return True