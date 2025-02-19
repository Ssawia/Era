from __future__ import annotations

from src.classes.entity_prototype import Character
import helpers
from helpers import log,Log
from random import choice, randint
from math import trunc

#Provavelmente isso não é a melhor maneira de implementar várias classes, mas por enquanto vai dar certo, confia
import src.classes.attacks.attackC as Attacks
import src.classes.damages.damageTypeC as dt
from src.classes.temp.temp_class_handler import Temp
import src.classes.effects.effect_class_prototype as Effect
from src.classes.debug import Debug



class Battle:

    def __init__(self, queue: list[Character]):
        self.turn = 0
        self.queue = queue
        self.isInCombat = False
        self.phase = ""
        self.pturn = False
        self.attacks_queue = []
        self.lenEnemy = 0
        self.lenPlayer = 0

        self.debug = Debug(battle_queue=self.queue,character=None)

    def menu_main(self, chara: Character):
        pass

    def menu_attack(self, chara: Character):
        attack: Attacks.Attack
        atk_i = 0
        damages = ""
        dmg: dt.DamageType
        for attack in chara.attacks:
            damages = ""
            for dmg in attack.dmgList:
                damages += f"|[{dmg.main_element}]{dmg.min_atk}-{dmg.max_atk}->"


            print(
                f"[{atk_i}][{attack.name}] Cost: {attack.cost} Hits: {attack.hits} Dmg: -> {damages} ")
            atk_i += 1

        print("[Escolha o ataque]")

        onMenu = True
        attacks_damage_list = []
        while onMenu:

            msg = int(input("ID: "))

            if len(chara.attacks) > msg >= 0:
                qt = chara.attacks[msg].targetLimit

                if helpers.check_cost(chara, msg, qt):
                    chara.attacks[msg].owner = chara
                    chara.attacks[msg].queue = self.queue
                    chara.attacks[msg].ai = False
                    
                    chara.attacks[msg].choice_player()
                    attacks_damage_list.append(chara.attacks[msg])

                    onMenu = False

            else:
                print("Ataque inválido")
        
        chara.attack_slot = attacks_damage_list

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


    def turn_players(self):
        chara: Character
        for chara in self.queue:
            if chara.ai.typeAi == "Player":
                self.phase = "Menu"
                self.pturn = True
                self.turn_player(chara)

    def turn_player(self, chara: Character):
        chara.attributes.actions = chara.attributes.max_actions
        while self.pturn and self.check_battle_conditions():
            self.update_queue_stats()
            if chara.attributes.actions > 0:
                print("======================================================================")
                log(Log.INFO, f"{chara.name}", f"[Turn: {self.turn}]")
                log(Log.INFO,
                    f"HP: {chara.attributes.status.hp}/{chara.attributes.status.maxHp} MP: {chara.attributes.status.mp}/{chara.attributes.status.maxMp} SP: {chara.attributes.status.sp}/{chara.attributes.status.maxSp} SPD: {chara.attributes.battle_spd}",
                    f"[Player][{chara.nick}]")
                log(Log.INFO, f"Action: {chara.attributes.actions}/{chara.attributes.max_actions}")
                print("======================================================================")

                print("[1] Atacar")
                print("[2] Status")
                print("[3] Passar")
                print("[4] Debug")
                msg = input(f"> ")

                if msg == "1":
                    self.phase = "Attack"
                    self.menu_attack(chara)
                    chara.attributes.actions -= 1
                elif msg == "2":
                    self.phase = "Status"
                    self.menu_status()
                elif msg == "3":
                    print(self.queue[1].name)
                    self.phase = "Pass"
                    self.menu_pass(chara)
                elif msg == "4":
                    self.phase = "Debug"
                    self.debug.character = chara
                    self.debug.battle_queue = self.queue
                    self.debug.menu_debug()
            else:
                self.menu_pass(chara)




    def turn_enemy(self, chara: Character):

        if self.check_battle_conditions() and chara.is_alive():
            log(Log.INFO, f"{chara.name} turn", f"[Turn: {self.turn}]")
            log(Log.INFO,
                f"HP: {chara.attributes.status.hp}/{chara.attributes.status.maxHp} SPD: {chara.attributes.status.spd}",
                f"[Enemy][{chara.nick}]")
            
            self.menu_pass(chara)

    def chose_ia_attacks(self):
        chara: Character
        for chara in self.queue:
            if chara.ai.typeAi == "Enemy":
                print(f"{chara.name} está escolhendo o ataque..")
                attacks = chara.ai.decide_attack(chara, self.queue, on_enemy=True)
                chara.attack_slot = attacks
        

    

    def process_attacks(self):
        self.queue.sort(key=lambda x: x.attributes.battle_spd, reverse=True)

        for obj in self.queue:

            if obj.attack_slot is not None and len(obj.attack_slot) == 0:
                obj_target.attack_slot = None

            atks_to_remove_obj = []
            atks_to_remove_obj_target = []
            if obj.attack_slot is not None:
                for index,atk in enumerate(obj.attack_slot):
                    for obj_target in atk.queue:
                        if obj_target.attack_slot is not None and len(obj_target.attack_slot) >= 1:

                            atk_clash = obj_target.attack_slot[0]
                            print(f"[{obj.name}]{atk.name} | {atk_clash.name}[{obj_target.name}]")
                            self.clash_attack(atk,atk_clash)

                            atks_to_remove_obj.append(atk)
                            
                            if obj in atk_clash.queue:       
                                 atk_clash.queue.remove(obj)
                            else:
                                obj_to_remove = {"obj": obj_target, "atk": atk_clash}
                                atks_to_remove_obj_target.append(obj_to_remove)


                        elif obj_target.attack_slot is None or len(obj_target.attack_slot) == 0:
                            atk.doDamage()

                            if obj in atk_clash.queue:       
                                 atk_clash.queue.remove(obj)
                            else:
                                obj_to_remove = {"obj": obj_target, "atk": atk_clash}
                                atks_to_remove_obj_target.append(obj_to_remove)
                            
            else:
                print(f"{obj.name} não tem mais ataque")
            

            for atk_remove in atks_to_remove_obj:
                if atk_remove in obj.attack_slot:
                    obj.attack_slot.remove(atk_remove)
            
            for data in atks_to_remove_obj_target:
                obj = data['obj']
                atk_remove = data['atk']
                
                if atk_remove in obj.attack_slot:
                    obj.attack_slot.remove(atk_remove)
                
                        

        
                
    def clash_attack(self,hit: Attacks.Attack, hit_clash: Attacks.Attack):
        dmg: dt.DamageType
        dmg_c: dt.DamageType
        total_dmg = 0
        types = '|'

        dmg_list_1 = hit.dmgList
        dmg_list_2 = hit_clash.dmgList
        if len(dmg_list_1) >= len(dmg_list_2):           
            for index,dmg_1 in enumerate(dmg_list_1):
                if index > len(dmg_list_2) - 1:
                    
                    min_atk = dmg_1.min_atk
                    max_atk = dmg_1.max_atk
                    crit = hit.owner.attributes.status.crit
                    max_crit = hit.owner.attributes.status.maxCrit
                    dmg_bonus = hit.owner.attributes.elements[dmg_1.main_element]

                    roll = randint(min_atk + crit,max_atk + max_crit)
                    log(Log.INFO, f"[{index}][{hit.name} > | < {hit_clash.name}][{hit.owner.name}][{dmg_1.main_element}]{min_atk}(+{crit})-{max_atk}(+{max_crit})= {roll}")

                else:
                    min_atk = dmg_1.min_atk
                    max_atk = dmg_1.max_atk
                    crit = hit.owner.attributes.status.crit
                    max_crit = hit.owner.attributes.status.maxCrit
                    dmg_bonus = hit.owner.attributes.elements[dmg_1.main_element]

                    dmg_c = hit_clash.dmgList[index]
                    min_atk_c = dmg_c.min_atk
                    max_atk_c = dmg_c.max_atk
                    crit_c = hit_clash.owner.attributes.status.crit
                    max_crit_c = hit_clash.owner.attributes.status.maxCrit
                    dmg_bonus_c = hit_clash.owner.attributes.elements[dmg_c.main_element]

                    roll = randint(min_atk + crit,max_atk + max_crit)
                    roll_c = randint(min_atk_c + crit_c,max_atk_c + max_crit_c)
                    if roll > roll_c:
                        log(Log.INFO, f"[{index}][{hit.name} > | < {hit_clash.name}][{hit.owner.name}][{dmg_1.main_element}]{min_atk}(+{crit})-{max_atk}(+{max_crit})= {roll} > {roll_c} =(+{max_crit_c}){max_atk_c}-(+{crit_c}){min_atk_c}[{dmg_c.main_element}][{hit_clash.owner.name}][{index}]")
                    elif roll_c > roll:
                        log(Log.INFO, f"[{index}][{hit_clash.name} > | < {hit.name}][{hit.owner.name}][{dmg_1.main_element}]{min_atk}(+{crit})-{max_atk}(+{max_crit})= {roll} < {roll_c} =(+{max_crit_c}){max_atk_c}-(+{crit_c}){min_atk_c}[{dmg_c.main_element}][{hit_clash.owner.name}][{index}]")

            
        elif len(dmg_list_2) >= len(dmg_list_1):
            for index,dmg_1 in enumerate(dmg_list_2):
                if index > len(dmg_list_1) - 1:
                    min_atk = dmg_1.min_atk
                    max_atk = dmg_1.max_atk
                    crit = hit.owner.attributes.status.crit
                    max_crit = hit.owner.attributes.status.maxCrit
                    dmg_bonus = hit.owner.attributes.elements[dmg_1.main_element]

                    roll = randint(min_atk + crit,max_atk + max_crit)
                    log(Log.INFO, f"[{index}][{hit_clash.name} > | < {hit.name}][{hit_clash.owner.name}][{dmg_1.main_element}]{min_atk}(+{crit})-{max_atk}(+{max_crit})= {roll}")

                else:
                    min_atk = dmg_1.min_atk
                    max_atk = dmg_1.max_atk
                    crit = hit.owner.attributes.status.crit
                    max_crit = hit.owner.attributes.status.maxCrit
                    dmg_bonus = hit.owner.attributes.elements[dmg_1.main_element]

                    dmg_c = hit.dmgList[index]
                    min_atk_c = dmg_c.min_atk
                    max_atk_c = dmg_c.max_atk
                    crit_c = hit_clash.owner.attributes.status.crit
                    max_crit_c = hit_clash.owner.attributes.status.maxCrit
                    dmg_bonus_c = hit_clash.owner.attributes.elements[dmg_c.main_element]

                    roll = randint(min_atk + crit,max_atk + max_crit)
                    roll_c = randint(min_atk_c + crit_c,max_atk_c + max_crit_c)
                    if roll > roll_c:
                        log(Log.INFO, f"[{index}][{hit.name} > | < {hit_clash.name}][{hit.owner.name}][{dmg_1.main_element}]{min_atk}(+{crit})-{max_atk}(+{max_crit})= {roll} > {roll_c} =(+{max_crit_c}){max_atk_c}-(+{crit_c}){min_atk_c}[{dmg_c.main_element}][{hit_clash.owner.name}][{index}]")
                    elif roll_c > roll:
                        log(Log.INFO, f"[{index}][{hit.name} > | < {hit_clash.name}][{hit.owner.name}][{dmg_1.main_element}]{min_atk}(+{crit})-{max_atk}(+{max_crit})= {roll} < {roll_c} =(+{max_crit_c}){max_atk_c}-(+{crit_c}){min_atk_c}[{dmg_c.main_element}][{hit_clash.owner.name}][{index}]")
        
        print("======================================================================")


            














                    
            


    def update_queue(self):
        chara: Character
        for chara in self.queue:
            if not chara.alive:
                print(f"{chara.name} can't continue")
                self.queue.remove(chara)
            elif chara.attributes is None:
                print(f"{chara.name} dont have the Attributes Component")
                self.queue.remove(chara)


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
    
    def update_queue_stats(self):
        for chara in self.queue:
            chara.attributes.update_attributes()
            chara.attributes.update_status(True)
            chara.attributes.update_elements()
            chara.attributes.update_resistances()
            chara.update_damage_attacks()
    


    def roll_characters_speed(self):
        chara: Character
        for chara in self.queue:
            spd = chara.attributes.status.spd
            chara.attributes.battle_spd = randint(spd[0],spd[1])
            print(f"{chara.name} roll {chara.attributes.battle_spd} spd")



    def start_battle(self):
        self.isInCombat = True

        print("======================================================================")
        self.lines_battle_start('battle_start')

        while self.check_battle_conditions():
            self.attacks_queue = []
            self.roll_characters_speed()

            #chara: Character
            #lenght = len(self.queue) - 1
            #if self.turn > lenght:
                #self.turn = 0

            #chara = self.queue[self.turn]


            print("======================================================================")


            self.chose_ia_attacks()
            self.turn_players()
            self.process_attacks()
            
            #chara.attributes.temp_handler.update_time_turn(turn=1)
            #chara.effects_handler.process_effects()



            # if chara.ai.typeAi == "Player":
            # elif chara.ai.typeAi == "Enemy":
            #     self.turn_enemy(chara)




        print("The Battle has ended!.")