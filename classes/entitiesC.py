from __future__ import annotations
#Provavelmente isso não é a melhor maneira de implementar varias classes, mas por enquanto vai dar certo, confia

import classes.attackC


class Character:
    def __init__(self, data : dict, _type : str):
        self._id = data['_id']
        self._name = data['name']
        self.nick = data['nick']
        self.type = _type
        self.alive = True


        self._hp = data['hp']
        self._maxhp = self._hp
        self._atk = data['atk']
        self._atkM = data['atkM']
        self._def = data['def']
        self._defM = data['defM']
        self._spd = data['spd']

        

    def isAlive(self):
        if self._hp <= 0:
            self.alive = False


    def defend(self, damage : float, damageType : classes.attackC.DamageType):

        self.isAlive()

        if self.alive:
            if damageType.defType == "PhysicalDamage":
                damage_final = damage - self._def
            elif damageType.defType == "MagicalDamage":
                damage_final = damage - self._defM
            
            self.hp -= damage_final

    def attack(self, obj : Character, attack : classes.attackC.Attack):
        attack.doDamage(obj)










