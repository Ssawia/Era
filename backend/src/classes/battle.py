from __future__ import annotations

from src.classes.entity_prototype import Character
import helpers
from helpers import log,Log
from random import choice, randint
from math import trunc

#Provavelmente isso não é a melhor maneira de implementar várias classes, mas por enquanto vai dar certo, confia
import src.classes.attacks.attackC as Attacks
from src.classes.attacks.attackC import Instance,Attack
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
        self.instances_to_process = []

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

        while onMenu:

            msg = int(input("ID: "))

            if len(chara.attacks) > msg >= 0:
                qt = chara.attacks[msg].targetLimit

                if helpers.check_cost(chara, msg, qt):
                    chara.attacks[msg].owner = chara
                    chara.attacks[msg].queue = self.queue
                    chara.attacks[msg].ai = False

                    battle_queue = chara.attacks[msg].choice_player()

                    if chara.attacks[msg] not in chara.attack_slot:
                        log(Log.DEBUG, f"{chara.attacks[msg].name} does not exist in {chara.name} attack slot, adding...", f"[{chara.name}]")
                        instance = Instance(attack=chara.attacks[msg], queue=battle_queue,active=True,owner=chara)
                        chara.attack_slot.append(instance)



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

            
            attacks_slot_str = ""
            instance: Instance
            for instance in chara.attack_slot:
                names = "->"
                for obj in instance.queue:
                    names += f" {obj.name} |"
                attacks_slot_str += f"->[{instance.active}]{instance.attack.name}:{names}"
            
            print("======================================================================")
            log(Log.INFO, f"{chara.name}", f"[Turn: {self.turn}]")
            log(Log.INFO,
                f"HP: {chara.attributes.status.hp}/{chara.attributes.status.maxHp} MP: {chara.attributes.status.mp}/{chara.attributes.status.maxMp} SP: {chara.attributes.status.sp}/{chara.attributes.status.maxSp} SPD: {chara.attributes.battle_spd}",
                f"[Player][{chara.nick}]")
            log(Log.INFO, f"Action: {chara.attributes.actions}/{chara.attributes.max_actions} Attack Slot- {attacks_slot_str}")
            print("======================================================================")

            print("[1] Atacar")
            print("[2] Status")
            print("[3] Passar")
            print("[4] Debug")
            msg = input(f"> ")

            if msg == "1":
                self.phase = "Attack"
                if chara.attributes.actions > 0:
                    self.menu_attack(chara)
                    chara.attributes.actions -= 1
            elif msg == "2":
                self.phase = "Status"
                self.menu_status()
            elif msg == "3":
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
                chara.ai.decide_attack(chara, self.queue, on_enemy=True)
                
        

    

    def process_attacks(self):
        self.queue.sort(key=lambda x: x.attributes.battle_spd, reverse=True)
        index_enemy = 0


        helpers.line()
        for obj in self.queue:

            log(Log.INFO, f"{obj.name} Turn.", "[Battle]")
            log(Log.DEBUG, f"{obj.name} attacks slot: {obj.attack_slot}", f"[{obj.name}]")
            self.instances_to_process = []
            for instance in obj.attack_slot:
                if instance.active:
                    helpers.say_line(obj, "attack")
                    for obj_enemy in instance.queue:
                        log(Log.INFO, f"{obj.name} is using {instance.attack.name}, and it's hit {obj_enemy.name}.", f"[Battle]")
                        
                        # Onde os ataques se clasham // fazer que os ataques se deletem quando terminarem
                        if obj_enemy.alive and obj_enemy.attack_slot[index_enemy].active and obj_enemy.attack_slot is not None and len(obj_enemy.attack_slot) >= 1 and obj_enemy not in instance.exclusion_queue:
                            # Fazer oque o ataque tenha um clash especifico no futuro
                            instance_enemy = obj_enemy.attack_slot[index_enemy].attack
                            log(Log.DEBUG, f"{obj.name} is clashing with {obj_enemy.name} on {instance.attack.name}<->{instance_enemy.name}", f"[{obj.name}]")

                            result = self.clash_attack(instance.attack,instance_enemy)

                            points = result[0]
                            points_enemy = result[1]

                   
                            obj_mult_attack = False
                            enemy_mult_attack = False

                            if len(instance.queue) > 1:
                                obj_mult_attack = True
                                
                            if len(obj_enemy.attack_slot[index_enemy].queue) > 1:
                                enemy_mult_attack = True
                                
                                
                            log(Log.DEBUG, f"points: {points}  multitarget: {obj_mult_attack}", F"[{obj.name}]")
                            log(Log.DEBUG, f"points: {points_enemy} multitarget: {enemy_mult_attack}", F"[{obj_enemy.name}]")
                            if points > points_enemy:
                                log(Log.INFO, f"{obj.name} wins the Attack Clash against {obj_enemy.name} using {instance.attack.name}", f"[Battle]")
                                if not obj_mult_attack:
                                    data1 = {"destroy": True, "instance": instance, "obj": obj, "multarget": obj_mult_attack}
                                    self.instances_to_process.append(data1)
                                elif obj_mult_attack:
                                    data1 = {"destroy": False, "instance": instance, "obj": obj, "multarget": obj_mult_attack, "target-exclusion": obj_enemy}
                                    self.instances_to_process.append(data1)

                                data2 = {"destroy": True, "instance": obj_enemy.attack_slot[index_enemy], "obj": obj_enemy, "multarget": enemy_mult_attack}
                                self.instances_to_process.append(data2)

                                    

                            if points_enemy > points:
                                log(Log.INFO, f"{obj_enemy.name} wins the Attack Clash against {obj.name} using {instance_enemy.name}", f"[Battle]")
                                if not enemy_mult_attack:
                                    data1 = {"destroy": True, "instance": obj_enemy.attack_slot[index_enemy], "obj": obj_enemy, "multarget": enemy_mult_attack}
                                    self.instances_to_process.append(data1)
                                elif obj_mult_attack:
                                    data1 = {"destroy": False, "instance": obj_enemy.attack_slot[index_enemy], "obj": obj_enemy, "multarget": enemy_mult_attack, "target-exclusion": obj}
                                data2 = data1 = {"destroy": True, "instance": instance, "obj": obj, "multarget": obj_mult_attack}
                                self.instances_to_process.append(data2)


                            if points_enemy == points:
                                log(Log.INFO, f"The Attack Clash between {obj.name} and {obj_enemy.name} ended in a draw.", f"[Battle]")


                        else:
                            log(Log.DEBUG,f"{instance.attack.name} no clash on {obj_enemy.name} attacks", f"[{obj.name}]")
                            result = self.direct_attack(instance.attack, obj_enemy)
                            points = result[0]
                            points_enemy = result[1]

                            if points > points_enemy:
                                if not obj_mult_attack:
                                    data1 = {"destroy": True, "instance": instance, "obj": obj, "multarget": obj_mult_attack}
                                    self.instances_to_process.append(data1)
                                elif obj_mult_attack:
                                    data1 = {"destroy": False, "instance": instance, "obj": obj, "multarget": obj_mult_attack, "target-exclusion": obj_enemy}
                                    self.instances_to_process.append(data1)

                        self.process_instances()

                input()
                helpers.line()
            

    def process_instances(self):
        for object_remove in self.instances_to_process:
            obj_character: Character
            instance_object: Instance
            
            multarget = object_remove["multarget"]
            obj_character = object_remove["obj"]
            destroy = object_remove['destroy']
            instance_object = object_remove['instance']


            if destroy and not multarget and instance_object in obj_character.attack_slot:
                instance_object.active = False
                log(Log.DEBUG,f"{instance_object.attack.name} has no multarget, disabling..", f"[{obj_character.name}]")

                #log(Log.INFO, f"{obj_character.name}'s {instance_object.attack.name} attack was destroyed in this clash.","[Battle]")
                                    

            if not destroy and multarget:
                obj_to_exclusion = object_remove['target-exclusion']
                instance_object.exclusion_queue.append(obj_to_exclusion)
                instance_object.check()
                log(Log.DEBUG,f"Instance has Multarget, add {obj_to_exclusion.name} to exclusion list.", f"[{obj_character.name}][{instance_object.attack.name}]")
                #log(Log.INFO,f"{obj_character.name} will ignore {obj_to_exclusion.name} for the next target.", f"[{obj_character.name}][{instance_object.attack.name}]")
            
            instance_object.check()
        
        self.instances_to_process = []

    
    def direct_attack(self,hit: Attacks.Attack, obj: Character):
        dmg_obj: dt.DamageType

        hit_points = 0
        hit_clash_points = 0

        for index,dmg_obj in enumerate(hit.dmgList):
            min_atk = dmg_obj.min_atk
            max_atk = dmg_obj.max_atk
            crit = hit.owner.attributes.status.crit
            max_crit = hit.owner.attributes.status.maxCrit
            dmg_bonus = hit.owner.attributes.elements[dmg_obj.main_element]
            log(Log.DEBUG, f"Damage Name: {dmg_obj.name} Rolls: {min_atk}(+{crit})-{max_atk}(+{max_crit}) Bonus: {dmg_bonus}", f"[{index}][{hit.owner.name}][{hit.name}]")

            roll = randint(min_atk + crit,max_atk + max_crit)
            log(Log.INFO, f"[{index}][{hit.name} > | {obj.name}][{dmg_obj.main_element}]{min_atk}(+{crit})-{max_atk}(+{max_crit})= {roll}")
            result = obj.deal_damage(dmg_obj,roll,dmg_bonus,hit.owner)
            hit_points += 1
            log(Log.INFO,result)

            hit_points += 1
        
        return [hit_points,hit_clash_points]
                
    def clash_attack(self,hit: Attacks.Attack, hit_clash: Attacks.Attack):
        dmg_obj: dt.DamageType
        dmg_enemy: dt.DamageType

        hit_points = 0
        hit_clash_points = 0

        if len(hit.dmgList) < len(hit_clash.dmgList):
            log(Log.DEBUG, f"Hit Clash({hit_clash.name}) is greater than Hit({hit.name}), swithing position..", )
            hit_temp = hit
            hit = hit_clash
            hit_clash = hit_temp

        for index,dmg_obj in enumerate(hit.dmgList):
            min_atk = dmg_obj.min_atk
            max_atk = dmg_obj.max_atk
            crit = hit.owner.attributes.status.crit
            max_crit = hit.owner.attributes.status.maxCrit
            dmg_bonus = hit.owner.attributes.elements[dmg_obj.main_element]
            log(Log.DEBUG, f"Damage Name: {dmg_obj.name} Rolls: {min_atk}(+{crit})-{max_atk}(+{max_crit}) Bonus: {dmg_bonus}", f"[{index}][{hit.owner.name}][{hit.name}]")

            if index > len(hit_clash.dmgList) - 1:
                log(Log.DEBUG, f" has no attack left", f"[{index}][{hit_clash.owner.name}][{hit_clash.name}]")
                roll = randint(min_atk + crit,max_atk + max_crit)
                log(Log.INFO, f"[{index}][{hit.name} > | {hit_clash.name}][{dmg_obj.main_element}]{min_atk}(+{crit})-{max_atk}(+{max_crit})= {roll}")
                result = hit_clash.owner.deal_damage(dmg_obj,roll,dmg_bonus,hit.owner)
                hit_points += 1
                log(Log.INFO,result)
            else:
            
                dmg_enemy = hit_clash.dmgList[index]
                min_atk_enemy = dmg_enemy.min_atk
                max_atk_enemy = dmg_enemy.max_atk
                crit_enemy = hit_clash.owner.attributes.status.crit
                max_crit_enemy = hit_clash.owner.attributes.status.maxCrit
                dmg_bonus_enemy = hit_clash.owner.attributes.elements[dmg_enemy.main_element]

                log(Log.DEBUG, f"Damage Name: {dmg_enemy.name} Rolls: {min_atk_enemy}(+{crit_enemy})-{max_atk_enemy}(+{max_crit_enemy}) Bonus: {dmg_bonus_enemy}", f"[{index}][{hit_clash.owner.name}][{hit_clash.name}]")

                roll = randint(min_atk + crit,max_atk + max_crit)
                roll_enemy = randint(min_atk_enemy + crit_enemy,max_atk_enemy + max_crit_enemy)

                if roll > roll_enemy:
                    log(Log.INFO, f"[{index}][{hit.name} > | < {hit_clash.name}][{hit.owner.name}][{dmg_obj.main_element}]{min_atk}(+{crit})-{max_atk}(+{max_crit})= {roll} > {roll_enemy} =(+{max_crit_enemy}){max_atk_enemy}-(+{crit_enemy}){min_atk_enemy}[{dmg_enemy.main_element}][{hit_clash.owner.name}][{index}]")
                    result = hit_clash.owner.deal_damage(dmg_obj,roll,dmg_bonus,hit.owner)
                    log(Log.INFO,result)
                    hit_points += 1
                elif roll_enemy > roll:
                    log(Log.INFO, f"[{index}][{hit.name} > | < {hit_clash.name}][{hit.owner.name}][{dmg_obj.main_element}]{min_atk}(+{crit})-{max_atk}(+{max_crit})= {roll} < {roll_enemy} =(+{max_crit_enemy}){max_atk_enemy}-(+{crit_enemy}){min_atk_enemy}[{dmg_enemy.main_element}][{hit_clash.owner.name}][{index}]")
                    result = hit.owner.deal_damage(dmg_enemy,roll_enemy,dmg_bonus_enemy,hit_clash.owner)
                    log(Log.INFO,result)
                    hit_clash_points += 1
                else:
                    log(Log.DEBUG, f" The clash deal draw", f"[{index}][{hit_clash.owner.name}][{hit_clash.name}]")

        
        return [hit_points,hit_clash_points]
        #adiciona os ataques a exclusão




 


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
            chara.update_instances()
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