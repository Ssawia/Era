from __future__ import annotations
from src.classes.entity_prototype import Character
import helpers
from helpers import log,Log
from random import choice

import src.classes.attacks.attackC as Attacks
from src.classes.temp.temp_class_handler import Temp
import src.classes.effects.effect_class_prototype as Effect


class Debug:
    def __init__(self, character: Character | None, battle_queue):
        self.character = character
        self.battle_queue = battle_queue

    def menu_debug(self) -> None:
        print("[2] Attributes")
        print("[3] Effects")
        print("[4] Temps")
        print("[5] Abilities")
        msg = input("debug> ")
        if msg == "2":
            self.debug_attributes()
        if msg == "3":
            self.debug_effect()
        if msg == "4":
            self.debug_temps()
        if msg == "5":
            self.debug_abilities()
    
    def debug_attributes(self):
        print("[1] Update Status")
        print("[2] Deal 1000 damage")

        msg = input("debug/attributes> ")
        if msg == "1":
            self.character.attributes.update_status(self.character, True)
        elif msg == "2":
            self.character.attributes.status.hp -= 1000
        
    def debug_effect(self):
        print("[1] Add Effect")
        print("[2] Process Effect")

        msg = input("debug/Effect> ")
        if msg == "1":
            effect = self.debug_create_effect()
            self.character.effects_handler.add_effects([effect])
        if msg == "2":
            self.character.effects_handler.process_effects()
        

    def debug_create_effect(self) -> Effect.Effect:
            
        print("[2] Default - AshenCurse")

        msg = input("> ")
        if msg == "2":
            effect_main = Effect.AshenCurse("ashen_curse",'Ashen Curse','The victim is marked with a smoldering brand that sears their flesh, slowly turning it to ash. This curse causes continuous burn damage over time, weakening both body and spirit. As the curse progresses, the afflicted’s movements become sluggish as their limbs blacken and crumble, and their resistance to fire-based attacks diminishes. Only through potent cleansing magic or a rare elemental salve can the curse be lifted, though scars remain, serving as a reminder of the fiery torment endured.',2,True,True,1,999,self.character,False,None,self.character)
            return effect_main


        

    def debug_temps(self):
        temps = ""
        print("======================================================================")
        for index,temp in enumerate(self.character.attributes.temp_handler.list_temps):
            temps += f"\n|-[{index}][{temp.typo}][TURN:{temp.turn}][TIME:{temp.time}][{temp.active_flag}]{temp.status}:{temp.value} "
        log(Log.INFO, f"Object Temps {temps}")


        print("======================================================================")
        print("[1] Create Temp")
        print("[2] Remove Temp")
        print("[3] Check Temps")
        print("[4] Check Temp Infos")

        msg = input("debug/temps> ")

        if msg == "1":
            temp = self.debug_create_temp()
            self.character.attributes.temp_handler.add_temp([temp])
        elif msg == "2":
            if len(self.character.attributes.temp_handler.list_temps) > 0:
                for index,temp in enumerate(self.character.attributes.temp_handler.list_temps):
                    log(Log.INFO,f"Status: {temp.status} Type: {temp.typo} Value: {temp.value} Flag: {temp.active_flag}", f"[Temp][{index}]")

                ab = input("> ")

                if ab.isnumeric():
                        
                    temp = self.character.attributes.temp_handler.list_temps[int(ab)]
                    self.character.attributes.temp_handler.remove_temp(list_temp=[temp])
                    self.character.attributes.temp_handler.update_temp()
                else:
                    self.character.attributes.temp_handler.remove_temp(flags=[ab])
                    self.character.attributes.temp_handler.update_temp()
            else:
                log(Log.WARNING, "Object has no temp to remove")


        elif msg == "3":
            if len(self.character.attributes.temp_handler.list_temps) > 0:
                for index,temp in enumerate(self.character.attributes.temp_handler.list_temps):
                    log(Log.INFO,f"Status: {temp.status} Type: {temp.typo} Value: {temp.value} Flag: {temp.active_flag}", f"[Temp][{index}]" )

            else:
                log(Log.WARNING, "Object has no temp to show")
        elif msg == "4":
            for key in self.character.attributes.temp_handler.temps_info.keys():
                data = self.character.attributes.temp_handler.temps_info[key]
                log(Log.INFO,f"{key}")
                for dta in data:
                    typo = ''
                    keys = list(dta.keys())
                    if keys[0] == 'add':
                        typo = "add"
                    else:
                        typo = "mult"
                    print(f"Type: {typo} Value: {dta[typo]} Turns: {dta['turns']} Time: {dta['time']}")
        
    def debug_create_temp(self) -> Temp:
        print("[1] Create")
        print("[2] Default")
        print("[3] Random")

        msg = input("> ")
            
        if msg == "1":
            status = input("Status: ")
            typo = input("Type: ")
            turn = int(input("Turn: "))
            time = int(input("Time: "))
            value = int(input("Value: "))
            active = bool(input("Activacted: "))
            is_turn = bool(input("isTurn: "))
            is_time = bool(input("isTime: "))
            flag = input("Flag: ")
            if len(flag) <= 0:
                flag = None
            tmp = Temp(status,typo,turn,time,value,active,is_turn,is_time,flag)
            return tmp
        elif msg == "2":
            tmp = Temp("atk","add",1,0,1000,True,True,False,"")
            return tmp
        elif msg == "3":
            status_choice = choice(['hp','Fire',])


    def debug_abilities(self):
        print("[1] Add Ability")
        print("[2] Delete all abilities")
        print("[3] Update Abilities")
        print("[4] Remove Ability")
        log(Log.INFO, f"Object Abilities: {self.character.abilities}")
        msg = input("debug/abilities> ")
        if msg == "1":
            ab = input("debug/abilities/add> ")
            if ab not in self.character.abilities and len(ab) > 0:
                self.character.abilities.append(ab)
                self.character.check_abilities()
            else:
                log(Log.WARNING, "Ability already exist in object")

        elif msg == "2":
            self.character.on_death_abylity()
        elif msg == "3":
            self.character.check_abilities()
        elif msg == "4":
            if len(self.character.abilities) > 0:
                for index,ability in enumerate(self.character.abilities):
                    log(Log.INFO,f" {ability}", f"[{index}]", "[Temp]")
                    ab = int(input("> "))
                    aby = self.character.abilities[ab]
                    self.character.attributes.temp_handler.remove_temp(flags=[aby])
                    self.character.abilities.remove(aby)
                    self.character.attributes.temp_handler.update_temp()
                            
                    log(Log.INFO, f"Ability {aby} from {self.character.nick} has removed.")
            else:
                log(Log.WARNING, "Object has no ability to remove")