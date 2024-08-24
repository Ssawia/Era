from __future__ import annotations
import json
from src.classes.entitiesC import Character
from typing import List

#Provavelmente isso não é a melhor maneira de implementar varias classes, mas por enquanto vai dar certo, confia

import src.classes.attacks.attackC as Attacks


config = json.load(open('config/config.json'))



chara_data = open(config["character_data"])
chara_data = json.load(chara_data)["characters"]




flande = Character(0,chara_data,"Enemy")
remilia = Character(1,chara_data,"Player")
sakuya = Character(2,chara_data,"Player")
fsakuya = Character(2,chara_data,"Enemy")





class Battle:

    def __init__(self, queue : List[Character]):
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
            print(f"[{atk_i}][{attack.name}] Cost: {attack.cost['mp']} Hits: {attack.hits}")
            atk_i += 1

        print("[Escolha o ataque]")

        onMenu = True
        
        while onMenu:

            msg = int(input("ID: "))

            if msg < len(chara.attacks) and msg >= 0:
                
                chara.attacks[msg].doDamage(chara,self.queue)
                onMenu = False
            else:
                print("Ataque inválido")




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
        print(f"[P][{chara.nick}] HP: {chara.attributes.status.hp}/{chara.attributes.status.maxHp} SPD: {chara.attributes.status.spd}")
        print("======================================================================")
        while self.pturn:
            print("[1] Atacar")
            print("[2] Passar")
            msg = int(input(f"Digite o menu: "))

            if msg == 1:
                self.phase = "Attack"
                self.menu_attack(chara)
                self.menu_pass(chara)
            elif msg == 2:
                self.phase = "Pass"
        print("======================================================================")



    def turn_enemy(self, chara : Character):
        print(f"Turn da {chara.name}")
        print(f"[E][{chara.nick}] HP: {chara.attributes.status.hp}/{chara.attributes.status.maxHp} SPD: {chara.attributes.status.spd}")
        chara.ai.decide_attack(chara,self.queue, onEnemy=True)
        self.menu_pass(chara)


    def sort_queue(self):
        self.queue.sort(key=lambda x: x.attributes.status.spd, reverse=True)


    

    def start_battle(self):
        self.isInCombat = True

        while self.isInCombat:
            chara : Character 
            lenght = len(self.queue) - 1

            if self.turn > lenght:
                self.turn = 0

            self.sort_queue()

            chara = self.queue[self.turn]
            

            if chara.ai.typeAi == "Player":
                self.phase = "Menu"
                self.pturn = True
                self.turn_player(chara)
            elif chara.ai.typeAi == "Enemy":
                self.turn_enemy(chara)

            
            

    






queue : List[Character] = [flande,remilia,sakuya,fsakuya]


battle =  Battle(queue)
battle.start_battle()
