from __future__ import annotations

from src.classes.entity_prototype import Character
import helpers
from helpers import log,Log
from random import choice

#Provavelmente isso não é a melhor maneira de implementar várias classes, mas por enquanto vai dar certo, confia
import src.classes.attacks.attackC as Attacks
from src.classes.temp.temp_class_handler import Temp



class Battle:

    def __init__(self, queue: list[Character]):
        self.turn = 0
        self.queue = queue
        self.isInCombat = False
        self.phase = ""
        self.pturn = False
        self.lenEnemy = 0
        self.lenPlayer = 0

    def menu_main(self, chara: Character):
        pass

    def menu_attack(self, chara: Character):
        attack: Attacks.Attack
        atk_i = 0
        for attack in chara.attacks:
            print(
                f"[{atk_i}][{attack.name}] Cost: {attack.cost['mp']} Hits: {attack.hits} Dmg: {attack.get_total_dmg()} ")
            atk_i += 1

        print("[Escolha o ataque]")

        onMenu = True

        while onMenu:

            msg = int(input("ID: "))

            if len(chara.attacks) > msg >= 0:

                chara.attacks[msg].doDamage(chara, self.queue)
                onMenu = False

            else:
                print("Ataque inválido")

    def menu_skills(self, chara: Character):
        pass

    def menu_items(self, chara: Character):
        pass

    def menu_status(self):
        helpers.show_info_queue(self.queue)

    def menu_pass(self, chara: Character):
        self.phase = ""
        self.pturn = False
        self.turn += 1

    def turn_player(self, chara: Character):
        while self.pturn and self.check_battle_conditions():
            print("======================================================================")
            log(Log.INFO, f"{chara.name} turn", f"[Turn: {self.turn}]")
            log(Log.INFO,
                f"HP: {chara.attributes.status.hp}/{chara.attributes.status.maxHp} SPD: {chara.attributes.status.spd}",
                f"[Player][{chara.nick}]")
            print("======================================================================")

            print("[1] Atacar")
            print("[2] Status")
            print("[3] Passar")
            print("[4] Debug")
            msg = input(f"> ")

            if msg == "1":
                self.phase = "Attack"
                self.menu_attack(chara)
                self.menu_pass(chara)
            elif msg == "2":
                self.phase = "Status"
                self.menu_status()
            elif msg == "3":
                self.phase = "Pass"
                self.menu_pass(chara)
            elif msg == "4":
                self.phase = "Debug"
                self.menu_debug(chara)


    def menu_debug(self,chara: Character) -> None:
        print("[4] Temps")
        print("[5] Abilities")
        msg = input("debug> ")
        if msg == "4":
            self.debug_temps(chara)
        if msg == "5":
            self.debug_abilities(chara)
    

    def debug_temps(self, chara: Character):
        print("[1] Create Temp")
        print("[2] Remove Temp")
        print("[3] Check Temps")
        print("[4] Check Temp Infos")
        msg = input("debug/temps> ")

        if msg == "1":
            temp = self.debug_create_temp()
            chara.attributes.temp_handler.add_temp([temp])
        elif msg == "2":
            if len(chara.attributes.temp_handler.list_temps) > 0:
                for index,temp in enumerate(chara.attributes.temp_handler.list_temps):
                    log(Log.INFO,f"Status: {temp.status} Type: {temp.typo} Value: {temp.value} Flag: {temp.active_flag}", f"[Temp][{index}]")

                ab = input("> ")

                if ab.isnumeric():
                    
                    temp = chara.attributes.temp_handler.list_temps[int(ab)]
                    chara.attributes.temp_handler.remove_temp(list_temp=[temp])
                    chara.attributes.temp_handler.update_temp()
                else:
                    chara.attributes.temp_handler.remove_temp(flags=[ab])
                    chara.attributes.temp_handler.update_temp()
            else:
                log(Log.WARNING, "Object has no temp to remove")


        elif msg == "3":
            if len(chara.attributes.temp_handler.list_temps) > 0:
                for index,temp in enumerate(chara.attributes.temp_handler.list_temps):
                    log(Log.INFO,f"Status: {temp.status} Type: {temp.typo} Value: {temp.value} Flag: {temp.active_flag}", f"[Temp][{index}]" )

            else:
                log(Log.WARNING, "Object has no temp to show")
        elif msg == "4":
            for key in chara.attributes.temp_handler.temps_info.keys():
                data = chara.attributes.temp_handler.temps_info[key]
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
            tmp = Temp("Fire","add",0,0,1000,True,False,False, "Phoenix Blessing")
            return tmp
        elif msg == "3":
            status_choice = choice(['hp','Fire',''])


    def debug_abilities(self, chara: Character):
        print("[1] Add Ability")
        print("[2] Delete all abilities")
        print("[3] Update Abilities")
        print("[4] Remove Ability")
        log(Log.INFO, f"Object Abilities: {chara.abilities}")
        msg = input("debug/abilities> ")
        if msg == "1":
            ab = input("debug/abilities/add> ")
            if ab not in chara.abilities and len(ab) > 0:
                chara.abilities.append(ab)
                chara.check_abilities()
            else:
                log(Log.WARNING, "Ability already exist in object")

        elif msg == "2":
            chara.on_death_abylity()
        elif msg == "3":
            chara.check_abilities()
        elif msg == "4":
            if len(chara.abilities) > 0:
                for index,ability in enumerate(chara.abilities):
                    log(Log.INFO,f" {ability}", f"[{index}]", "[Temp]")
                    ab = int(input("> "))
                    aby = chara.abilities[ab]
                    chara.attributes.temp_handler.remove_temp(flags=[aby])
                    chara.abilities.remove(aby)
                    chara.attributes.temp_handler.update_temp()
                        
                    log(Log.INFO, f"Ability {aby} from {chara.nick} has removed.")
            else:
                log(Log.WARNING, "Object has no ability to remove")




    def turn_enemy(self, chara: Character):

        if self.check_battle_conditions():
            log(Log.INFO, f"{chara.name} turn", f"[Turn: {self.turn}]")
            log(Log.INFO,
                f"HP: {chara.attributes.status.hp}/{chara.attributes.status.maxHp} SPD: {chara.attributes.status.spd}",
                f"[Enemy][{chara.nick}]")
            chara.ai.decide_attack(chara, self.queue, on_enemy=True)
            self.menu_pass(chara)

    def update_queue(self):
        chara: Character
        for chara in self.queue:
            if not chara.alive:
                print(f"{chara.name} can't continue")
                self.queue.remove(chara)
            elif chara.attributes is None:
                print(f"{chara.name} dont have the Attributes Component")
                self.queue.remove(chara)

        self.queue.sort(key=lambda x: x.attributes.status.spd, reverse=True)

    def lines_battle_start(self, phrase: str):

        char: Character

        for char in self.queue:
            if helpers.check_line(phrase, char.lines):
                line = choice(char.lines[phrase])
                log(Log.CHAT,line,f"[{char.name}]")




    def get_len_types(self):
        char: Character
        self.lenEnemy = 0
        self.lenPlayer = 0
        for char in self.queue:
            if char.ai.typeAi == "Enemy":
                self.lenEnemy += 1
            elif char.ai.typeAi == "Player":
                self.lenPlayer += 1

    def check_battle_conditions(self):
        self.update_queue()
        self.get_len_types()
        if self.isInCombat and self.lenEnemy > 0 and self.lenPlayer > 0:
            return True
        else:
            return False

    def start_battle(self):
        self.isInCombat = True

        print("======================================================================")
        self.lines_battle_start('battle_start')

        while self.check_battle_conditions():

            chara: Character
            lenght = len(self.queue) - 1
            if self.turn > lenght:
                self.turn = 0

            chara = self.queue[self.turn]


            if chara.ai.typeAi == "Player":
                self.phase = "Menu"
                self.pturn = True
                self.turn_player(chara)
            elif chara.ai.typeAi == "Enemy":
                self.turn_enemy(chara)


            chara.attributes.temp_handler.update_time_turn(turn=1)


        print("The Battle has ended!.")