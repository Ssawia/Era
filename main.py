from __future__ import annotations
import json
from classes.entitiesC import Character

#Provavelmente isso não é a melhor maneira de implementar varias classes, mas por enquanto vai dar certo, confia

import classes.attackC as Attacks


chara_data = open('data/chara/characters.json')
chara_data = json.load(chara_data)["characters"]




flande = Character(0,chara_data,"Enemy")
remilia = Character(1,chara_data,"Player")
sakuya = Character(2,chara_data,"Player")





class Battle:

    def __init__(self, queue : list,):
        self.turn = 0
        self.queue = queue
        self.isInCombat = False
        self.phase = ""
        self.pturn = False

    

    def menu_main(self, chara : Character):
        pass

    def menu_attack(self, chara : Character):
        attack : Attacks.Attack
        atk_i = 0
        for attack in chara.attacks:
            final_dmg = 0
            for dmg in attack.damage:
                final_dmg += dmg
            print(f"[{atk_i}][{attack.name}][{attack.desc}] Damages: {attack.damage}|[{final_dmg}*{attack.hits}]|[{final_dmg*attack.hits}] Cost: {attack.cost['mp']} Hits: {attack.hits}")
            atk_i += 1

    def menu_skills(self,chara : Character):
        pass

    def menu_items(self, chara : Character):
        pass

    def menu_status(self,chara : Character):
        pass

    def menu_pass(self,chara : Character):
        self.phase = ""
        self.pturn = False
        self.turn += 1

    

    def turn_player(self, chara : Character):
        print(f"Turn da {chara.name}")
        print(f"[P][{chara.nick}] HP: {chara.attributes.hp}/{chara.attributes.maxHp} SPD: {chara.attributes.spd}")

        while self.pturn:

            msg = str(input(f"Digite o menu: "))

            if msg == "pass":
                self.phase = "Pass"
            if msg == "atk":
                self.phase = "Attack"





    def turn_enemy(self, chara : Character):
        print(f"Turn da {chara.name}")
        print(f"[E][{chara.nick}] HP: {chara.attributes.hp}/{chara.attributes.maxHp} SPD: {chara.attributes.spd}")
        input()
        self.turn += 1

    def turn_pass(self):
        pass


    def sort_queue(self):
        self.queue.sort(key=lambda x: x._spd, reverse=True)

    

    def start_battle(self):
        self.isInCombat = True

        while self.isInCombat:
            chara : Character 
            lenght = len(self.queue) - 1

            if self.turn > lenght:
                self.turn = 0

            self.sort_queue()

            chara = self.queue[self.turn]
            

            if chara.type == "Player":
                self.phase = "Menu"
                self.pturn = True
                self.turn_player(chara)
            elif chara.type == "Enemy":
                self.turn_enemy(chara)

            
            

    






queue = [flande,remilia,sakuya]


battle =  Battle(queue=queue)
battle.start_battle()
