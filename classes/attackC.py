from __future__ import annotations

import classes.entitiesC as Chara
import classes.damageTypeC as dmgType
import sys
import json


#Classe usada para definir o tipo de dano dos ataques, como ataque fisico ou ataque magico
class Attack:
    def __init__(self, name : str, desc : str,  damage : list, cost : dict, hits : int, dmgType : list):
        self.name = name
        self.desc = desc
        self.damage = damage
        self.cost = cost
        self.hits = hits
        self.types = dmgType
    

    def checkCost(self, owner : Chara.Character):
        canAttack = False
        # Simplesmente a maneira mais merda de fazer isso, mas por enquanto da pro gasto
        for key in self.cost.keys():
            if key == "mp":
                if owner.attributes.mp >= self.cost[key]:
                    owner.attributes.mp -= self.cost[key]
                    canAttack = True
        

        return canAttack
                    
                

    
    def doDamage(self):
        pass

    def imwho(self):
       return self.name
    
class PhysicalAttack(Attack):
    def __init__(self,name,desc,damage,cost,hits,dmgType):
        super().__init__(name=name, desc=desc,damage=damage,cost=cost,hits=hits,dmgType=dmgType)
    
    def doDamage(self, owner : Chara.Character, obj: Chara.Character):
        
        i : dmgType.DamageType = None
        dmgList  = []

        for i in self.types:
            i.setAttack(owner)
            dmgList.append(i)    

        for c in range(self.hits):
            obj.defend(dmgList)

        return True
        


class MagicalAttack(Attack):
    def __init__(self,name,desc,damage,cost,hits,dmgType):
        super().__init__(name=name, desc=desc,damage=damage,cost=cost,hits=hits,dmgType=dmgType)
    
    def doDamage(self, owner : Chara.Character, obj: Chara.Character):
        
        i : dmgType.DamageType = None
        dmgList  = []

        for i in self.types:
            i.setAttack(owner)
            dmgList.append(i)
            
        for c in range(self.hits):
            obj.defend(dmgList)
            
        return True



        





def getAttackClass(data : list):
    attacks_data = open('data/attacks/attacks.json')
    attacks_data = json.load(attacks_data)["physicalAttack"]

    damage_data = open('data/damageTypes/damagesType.json')
    damage_data = json.load(damage_data)["DamagesType"]

    attacks_list = []

    for c in data:
        atk_data : dict = attacks_data[c]
        damagetypes : dmgType.DamageType = dmgType.getDamageTypeClass(atk_data['type'], damage_data, atk_data['damage'])

        basicAttack : Attack = str_to_class(attacks_data[c]['class'])(name=attacks_data[c]['name'],desc=attacks_data[c]['desc'], damage=attacks_data[c]['damage'], cost= attacks_data[c]['cost'], hits = attacks_data[c]['hits'], dmgType = damagetypes)
        attacks_list.append(basicAttack)
    
    return attacks_list







def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)