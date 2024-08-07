from __future__ import annotations

import classes.entitiesC as Chara
import classes.damageTypeC as dmgType
import sys
import json


#Classe usada para definir o tipo de dano dos ataques, como ataque fisico ou ataque magico
class Attack:
    def __init__(self, _id : int, _class : str, name : str, desc : str, target : str, targetLimit : int, intent : str, damage : list, cost : dict, cooldown : float ,hits : int, dmgType : list):
        self._id = _id
        self._class = _class
        self.name = name
        self.desc = desc
        self.target = target
        self.targetLimit = targetLimit
        self.intent = intent
        self.damage = damage
        self.cost = cost
        self.cooldown = cooldown
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
    def __init__(self,_id,_class,name,desc,target,targetLimit,intent,damage,cost,cooldown,hits,dmgType):
        super().__init__(_id=_id, _class=_class, name=name, desc=desc,target=target,targetLimit=targetLimit,intent=intent,damage=damage,cost=cost,cooldown=cooldown,hits=hits,dmgType=dmgType)
    
    def doDamage(self, owner : Chara.Character, objs: list):
        
        obj : Chara.Character = None

        i : dmgType.DamageType = None
        dmgList  = []

        for i in self.types:
            i.setAttack(owner)
            dmgList.append(i)    

        for obj in objs:
            for c in range(self.hits):
                obj.defend(dmgList)

        return True
        


class MagicalAttack(Attack):
    def __init__(self,_id,_class,name,desc,target,targetLimit,intent,damage,cost,cooldown,hits,dmgType):
        super().__init__(_id=_id, _class=_class, name=name, desc=desc,target=target,targetLimit=targetLimit,intent=intent,damage=damage,cost=cost,cooldown=cooldown,hits=hits,dmgType=dmgType)
    
    def doDamage(self, owner : Chara.Character, objs: list):
        
        obj : Chara.Character = None

        i : dmgType.DamageType = None
        dmgList  = []

        for i in self.types:
            i.setAttack(owner)
            dmgList.append(i)
        
        for obj in objs:
            for c in range(self.hits):
                obj.defend(dmgList)
            
        return True


class HealingAttack(Attack):
    def __init__(self,_id,_class,name,desc,target,targetLimit,intent,damage,cost,cooldown,hits,dmgType):
        super().__init__(_id=_id, _class=_class, name=name, desc=desc,target=target,targetLimit=targetLimit,intent=intent,damage=damage,cost=cost,cooldown=cooldown,hits=hits,dmgType=dmgType)
    

    def doDamage(self, owner : Chara.Charactert, objs: list):

        obj : Chara.Character = None

        pass

        



        





def getAttackClass(data : list):
    attacks_data = open('data/attacks/attacks.json')
    attacks_data = json.load(attacks_data)["physicalAttack"]

    damage_data = open('data/damageTypes/damagesType.json')
    damage_data = json.load(damage_data)["DamagesType"]

    attacks_list = []

    for c in data:
        atk_data : dict = attacks_data[c]
        damagetypes : dmgType.DamageType = dmgType.getDamageTypeClass(atk_data['type'], damage_data, atk_data['damage'])


        #melhorar essa merda kkkkkkkk
        basicAttack : Attack = str_to_class(attacks_data[c]['class'])(
            _id =attacks_data[c]['_id'],
            _class =attacks_data[c]['class'],
            name=attacks_data[c]['name'],
            desc=attacks_data[c]['desc'],
            target=attacks_data[c]['target'],
            targetLimit=attacks_data[c]['target-limit'],
            intent=attacks_data[c]['intent'],
            damage=attacks_data[c]['damage'],
            cost= attacks_data[c]['cost'],
            cooldown = attacks_data[c]['cooldown'],
            hits = attacks_data[c]['hits'],
            dmgType = damagetypes)
        attacks_list.append(basicAttack)
    
    return attacks_list




def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)