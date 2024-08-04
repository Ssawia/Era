import json
from classes.entitiesC import Character


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
        self.phase = ""
        self.pturn = False
    

    def turn_player(self, chara : Character):
        print(f"Turn da {chara._name}")
        print(f"[P][{chara.nick}] HP: {chara._hp}/{chara._maxhp} SPD: {chara._spd}")

        while self.pturn:

            if self.phase == "Menu":
                pass
            elif self.phase == "Attack":
                pass
            elif self.phase == "Skills":
                pass
            elif self.phase == "Items":
                pass
            elif self.phase == "Status":
                pass
            elif self.phase == "Pass":
                self.phase = ""
                self.pturn = False
                self.turn += 1



    def turn_enemy(self, chara : Character):
        print(f"Turn da {chara._name}")
        print(f"[E][{chara.nick}] HP: {chara._hp}/{chara._maxhp} SPD: {chara._spd}")
        input()
        self.turn += 1

    def turn_pass(self):
        pass


    def sort_queue(self):
        self.queue.sort(key=lambda x: x._spd, reverse=True)

    

    def start_battle(self):
        self.isInCombat = True

        while self.isInCombat:
            chara : Character = None
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
