from __future__ import annotations
import src.classes.entity_prototype as ch
import src.classes.temps.temp_class_handler as tp

import uuid
from helpers import log, Log
from math import trunc
import abstraction


class Effect:
    def __init__(self, typo, name, desc, turns, active, is_stackable,stacks, max_stacks, giver, character, has_temp, temp_objs, obj_values, event):
        self.uuid = uuid.uuid4()
        self.typo = typo
        self.name = name
        self.desc = desc
        self.main_turn = turns
        self.turn = self.main_turn
        self.active = active
        self.is_stackable = is_stackable
        self.main_stacks = stacks
        self.stacks = self.main_stacks

        self.max_stacks = max_stacks
        self.has_temp = has_temp

        self.temp_objs =  temp_objs
        self.objs_temp_data = []
        self.obj_values= obj_values
        self.event = event


        self.owner : ch.Character = character
        self.giver: ch.Character | None = giver
        self.start()
    

    def start(self):
        #print(self.obj_values)
        pass
        
    

    def init_effect(self):
        if self.active and self.name not in self.owner.attributes.temp_handler.flags:
            for temp_obj in self.temp_objs:
                if temp_obj["event"] == "init":
                    temp_id = temp_obj['id']
                    temp_target = temp_obj['target']
                    temp_flag = temp_obj["flag"]
                    
                    owner: ch.Character

                    if temp_target == "self":
                        owner = self.giver
                    elif temp_target == "target":
                        owner = self.owner
                    
                    temp = abstraction.get_temp_from_id(temp_id,temp_flag)
                    owner.attributes.temp_handler.add_temp([temp])

                    temp_data = {"obj": self.giver, "temp": temp, "flag": temp_flag}
                    self.objs_temp_data.append(temp_data)

                    owner.attributes.update_attributes()
                    owner.attributes.update_attributes_bonus()
                    owner.attributes.update_elements()
                    owner.attributes.update_resistances()


    def process_effect(self):
        pass

    def end_effect(self):
        self.active = False
        log(Log.INFO,f"Effect {self.name} has ended", f"[{self.owner.name}][EffectHandler][Effect]")

        if self.has_temp:
            for data in self.objs_temp_data:
                obj: ch.Character
                flag = data['flag']
                obj = data['obj']
                
                if flag == self.name:
                    log(Log.INFO, f"{obj.name} tem a flag {self.name} temp, removendo", f"[{obj.name}][EffectHandler][Effect]")
                    obj.attributes.temp_handler.remove_temp(flags=[self.name])
                



