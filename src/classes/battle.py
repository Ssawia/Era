from __future__ import annotations

from src.classes.entitiesC import Character
import helpers
from random import choice

#Provavelmente isso não é a melhor maneira de implementar várias classes, mas por enquanto vai dar certo, confia
import src.classes.attacks.attackC as Attacks




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
        print(f"{chara.name} turn.")
        print(
            f"[P][{chara.nick}] HP: {chara.attributes.status.hp}/{chara.attributes.status.maxHp} SPD: {chara.attributes.status.spd}")
        print("======================================================================")
        while self.pturn and self.check_battle_conditions():
            print("[1] Atacar")
            print("[2] Status")
            print("[3] Passar")
            msg = int(input(f"Digite o menu: "))

            if msg == 1:
                self.phase = "Attack"
                self.menu_attack(chara)
                self.menu_pass(chara)
            elif msg == 2:
                self.phase = "Status"
                self.menu_status()
            elif msg == 3:
                self.phase = "Pass"
                self.menu_pass(chara)

    def turn_enemy(self, chara: Character):

        if self.check_battle_conditions():
            print(f"{chara.name} turn.")
            print(
                f"[E][{chara.nick}] HP: {chara.attributes.status.hp}/{chara.attributes.status.maxHp} SPD: {chara.attributes.status.spd}")
            chara.ai.decide_attack(chara, self.queue, onEnemy=True)
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
                print(f"{char.name}: {line}")

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
        print("======================================================================")

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

        print("The Battle has ended!.")