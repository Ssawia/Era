from __future__ import annotations
#Provavelmente isso não é a melhor maneira de implementar varias classes, mas por enquanto vai dar certo, confia

import classes.attackC as Attacks
import classes.damageTypeC as damageTypes

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

        self.attacks = data['attacks']
        self.getAttacks()

    

    def get_status(self):
        print(f"[{self._name}] HP: {self.attributes.hp}/{self.attributes.maxHp} MP: {self.attributes.mp}/{self.attributes.maxMp}")


    def getAttacks(self):
        self.attacks = Attacks.getAttackClass(self.attacks)



    def isAlive(self):
        if self._hp <= 0:
            self.alive = False


    def defend(self, damagesType : list):

        self.isAlive()
        dmgType : damageTypes.DamageType = None

        if self.alive:
            for dmgType in damagesType:
                if dmgType.defType == "PhysicalDamage":
                    dmg = dmgType.atk - self.attributes.df
                    self.attributes.hp -= dmg
                    print(f"{self._name} tomou {dmgType.atk}-{self.attributes.df}={dmg} de dano")
                elif dmgType.defType == "MagicalDamage":
                    dmg = dmgType.atk - self.attributes.dfm
                    self.attributes.hp -= dmg
                    print(f"{self._name} tomou {dmgType.atk}-{self.attributes.dfm}={dmg} de dano")
        else:
            print("Já está morto")
    

    def healing(self,damageTypes : list):
        
        self.isAlive()
        dmgType : damageTypes.DamageType = None

        if self.isAlive:
            for dmgType in damageTypes:
                if self.attributes.hp + dmgType.heal < self.attributes.maxHp:
                    self.attributes.hp += dmgType.heal
        else:
            print("Já está morto, não tem como curar")


    def attack(self, obj : Character, attack : Attacks.Attack):
        attack.doDamage(obj)










