from __future__ import annotations
#Provavelmente isso não é a melhor maneira de implementar varias classes, mas por enquanto vai dar certo, confia

import classes.attacks.attackC as Attacks
import classes.damages.damageTypeC as damageTypes
from typing import List

import abstraction

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
    def __init__(self, _id : int, data : dict, _type : str):
        data = next((sub for sub in data if sub['_id'] == _id))

        self._id = data['_id']
        self.name = data['name']
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

        self.attacks: List[Attacks.Attack] = data['attacks']
        self.getAttacks()

    

    def get_status(self):
        try:
            print(f"[{self.name}] HP: {self.attributes.hp}/{self.attributes.maxHp} MP: {self.attributes.mp}/{self.attributes.maxMp}")
            return True
        except Exception as E:
            return False


    def getAttacks(self):
        self.attacks = abstraction.getAttackClass(self.attacks)



    def isAlive(self):
        if self._hp <= 0:
            self.alive = False


    def defend(self, damagesType : list):

        self.isAlive()
        dmgType : damageTypes.DamageType

        if self.alive:
            # Uma bela maneira de spammar o cli, favor consertar depois
            for dmgType in damagesType:
                if dmgType.defType == "PhysicalDamage":
                    dmg = dmgType.atk - self.attributes.df
                    self.attributes.hp -= dmg
                    print(f"{self.name} tomou {dmgType.atk}-{self.attributes.df}={dmg} de dano")
                elif dmgType.defType == "MagicalDamage":
                    dmg = dmgType.atk - self.attributes.dfm
                    self.attributes.hp -= dmg
                    print(f"{self.name} tomou {dmgType.atk}-{self.attributes.dfm}={dmg} de dano")
        else:
            print("Já está morto")
    

    def healing(self,damageTypes : list):
        
        self.isAlive()
        dmgType : damageTypes.DamageType
        
        if self.isAlive:
            
            for dmgType in damageTypes:
                
                if self.attributes.hp + dmgType.heal < self.attributes.maxHp:
                    print(f"[{self.name}][HP:{self.attributes.hp}/{self.attributes.maxHp}] curou {dmgType.heal} e ficou com {self.attributes.hp + dmgType.heal} de vida")
                    self.attributes.hp += dmgType.heal
                else:
                    print(f"[{self.name}][HP:{self.attributes.hp}/{self.attributes.maxHp}] curou {dmgType.heal} e ficou com {self.attributes.hp} de vida")
        else:
            print("Já está morto, não tem como curar")











