from __future__ import annotations
#Provavelmente isso não é a melhor maneira de implementar varias classes, mas por enquanto vai dar certo, confia

import classes.attackC

class Attributes:
    def __init__(self, hp,mp,atk,atkm,df,dfm,spd):
        self.hp = hp
        self.maxHp = self.hp
        self.mp = mp
        self.maxMp = self.mp
        self.atk = atk
        self.atkm = atkm
        self.df = df
        self.dfm = dfm
        self.spd = spd
        


class Character:
    def __init__(self, data : dict, _type : str):
        self._id = data['_id']
        self._name = data['name']
        self.nick = data['nick']
        self.type = _type
        self.alive = True


        self._hp = data['hp']
        self._mp = data['mp']
        self._atk = data['atk']
        self._atkM = data['atkM']
        self._def = data['def']
        self._defM = data['defM']
        self._spd = data['spd']

        self.attributes : Attributes = Attributes(self._hp,self._mp,self._atk,self._atkM,self._def,self._defM,self._spd)

        

    def isAlive(self):
        if self._hp <= 0:
            self.alive = False


    def defend(self, damage : float, damageType : classes.attackC.DamageType):

        self.isAlive()

        if self.alive:
            if damageType.defType == "PhysicalDamage":
                damage_final = damage - self.attributes.df
            elif damageType.defType == "MagicalDamage":
                damage_final = damage - self.attributes.dfm
            
            self.attributes.hp -= damage_final
        else:
            print("Já está morto")

    def attack(self, obj : Character, attack : classes.attackC.Attack):
        attack.doDamage(obj)










