from __future__ import annotations
import src.classes.entity_prototype as ch
import src.classes.temps.temp_class_handler as tp

import uuid
from helpers import log, Log
from math import trunc
import abstraction


class Effect:
    def __init__(self, typo, name, desc, turns, active, is_stackable,stacks, max_stacks, character,has_temp, temp_objs,temp_owner, giver = None):
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
        self.temp_objs: list[tp.Temp] = temp_objs
        self.temp_owner: ch.Character | ch.Attributes = temp_owner
        self.owner : ch.Character = character
        self.giver: ch.Character | None = giver
    

    def init_effect(self):
        if self.active:
            if self.name not in self.owner.attributes.temp_handler.flags:
                for temp_obj in self.temp_objs:
                    if temp_obj["event"] == "init":
                        temp_id = temp_obj['id']
                        temp_target = temp_obj['target']
                        temp_flag = temp_obj["flag"]
                        temp_data = abstraction.get_data_from_id(temp_id,abstraction.temps_data, "[Temps]")

                        if temp_target == "self":
                            temp = tp.Temp(temp_data['name'], temp_data['status'], temp_data['typo'], temp_data["turn"], temp_data["time"],temp_data["value"],True,temp_data["is_turn"], temp_data["is_time"],temp_flag)
                            self.giver.attributes.temp_handler.add_temp([temp])
                            self.giver.attributes.update_attributes()
                            self.giver.attributes.update_attributes_bonus()
                            self.giver.attributes.update_elements()
                            self.giver.attributes.update_resistances()
                            log(Log.INFO, f"{temp.name} on {self.giver.name} for {temp.turn} turn.", "[Temp]")
                        elif temp_target == "target":
                            temp = tp.Temp(temp_data['name'], temp_data['status'], temp_data['typo'], temp_data["turn"], temp_data["time"],temp_data["value"],True,temp_data["is_turn"], temp_data["is_time"],temp_flag)
                            self.owner.attributes.temp_handler.add_temp([temp])
                            log(Log.INFO, f"{temp.name} on {self.owner.name} for {temp.turn} turn.", "[Temp]") 

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



