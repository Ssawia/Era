

import json
from character import Character


chara_data = open('data/chara/characters.json')
chara_data = json.load(chara_data)["characters"]




flande = Character(chara_data[0],"Enemy")
remilia = Character(chara_data[1],"Player")
sakuya = Character(chara_data[2],"Player")





class Battle:

    def __init__(self, queue : list,):
        self.turn = 0
        self.queue = queue
        self.isInCombat = False
    

    def turn_attack_player(self, chara : Character):
        print(f"Turn da {chara._name}")
        print(f"[P][{chara.}]")
        input()
        self.turn += 1

    def turn_attack_enemy(self, chara : Character):
        print(f"Turn da {chara._name}*")
        input()
        self.turn += 1

    def turn_pass(self):
        pass
    

    def start_battle(self):
        self.isInCombat = True

        while self.isInCombat:
            chara : Character = None
            lenght = len(self.queue) - 1

            if self.turn > lenght:
                self.turn = 0
            
            chara = self.queue[self.turn]

            if chara.type == "Player":
                self.turn_attack_player(chara)
            elif chara.type == "Enemy":
                self.turn_attack_enemy(chara)

            
            

    






queue = [flande,remilia,sakuya]


battle =  Battle(queue=queue)
battle.start_battle()
