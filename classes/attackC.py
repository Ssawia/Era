from __future__ import annotations

import classes.entitiesC as Chara
import classes.damageTypeC as dmgType
import sys
import json

# Depois de alguns minutos de filosofia, eu cheguei a conclusão que single e select é literalmente a mesma coisa, só muda o limite do ataque 🤡
# Vou deixar por enquanto, motivo ? preguiça

class Selector:
    def __init__(self,name : str , queue : list, target : str, target_limit : int, intent: str):
        self.attack_name = name
        self.queue = queue
        self.target = target
        self.target_limit = target_limit
        self.intent = intent
        self.listt = []

    
    def get_intent_on_queue(self, onEnemy : bool = False):
        chara : Chara.Character = None
        selected = []


        match self.intent:
            # Top 10 codigos fodas 2024
            case "help":
                for chara in self.queue:
                    if not onEnemy:
                        if chara.type == "Player":
                            selected.append(chara)
                    elif onEnemy:
                        if chara.type == "Enemy":
                            selected.append(chara)                       
                
            case "harm":
                for chara in self.queue:
                    if not onEnemy:
                        if chara.type == "Enemy":
                            selected.append(chara)
                    elif onEnemy:
                        if chara.type == "Player":
                            selected.append(chara)
                
            case "harmall":
                selected = self.queue
                
            case _:
                selected = self.queue
        
        return selected
    
    def remove_select(self):
        pass


    def select_in_queue(self):
        chara : Chara.Character = None
        self.listt = self.get_intent_on_queue()
        selected = []
        idS = 0

        print(f"[{self.attack_name}][{self.intent}][{self.target}] Selecione {self.target_limit} alvo(s)")


        
        for c in range(self.target_limit):
            idL = 0
            print("==========================[Lista]==============================")
            for chara in self.listt:
                print(f"[{idL}][{chara.name}] HP : {chara.attributes.hp}/{chara.attributes.maxHp}")
                idL += 1

            msg = str(input("Selecione o ID: "))
            msg = int(msg)

            if msg <= len(self.listt) - 1:
                selected.append(self.listt[msg])
                self.listt.remove(self.listt[msg])

            print("==========================[Selecionados]==============================")
            for chara in selected:
                
                print(f"[{idS}][{chara.name}] HP : {chara.attributes.hp}/{chara.attributes.maxHp}")

                idS += 1
            print("="*70)

        
        return selected
        


    def self_attack(self,owner):
        self.listt = []
        self.listt.append(owner)

        return self.listt

    def single_attack(self):
        return self.select_in_queue()

    def multi_attack(self):
        self.listt = self.get_intent_on_queue()
        return self.listt
        

    def select_attack(self):
        return self.select_in_queue()

    


#Classe usada para definir o tipo de dano dos ataques, como ataque fisico ou ataque magico
class Attack:
    def __init__(self, _id : int, _class : str, name : str, desc : str, target : str, targetLimit : int, intent : str, damage : list, cost : dict ,hits : int, dmgType : list):
        self._id = _id
        self._class = _class
        self.name = name
        self.desc = desc
        self.target = target
        self.targetLimit = targetLimit
        self.intent = intent
        self.damage = damage
        self.cost = cost
        self.hits = hits
        self.types = dmgType
        self.select : Selector = None
    

    def check_target(self, owner : Chara.Character):
        queue = []
        if self.target == "select":
            queue = self.select.select_attack()
        elif self.target == "single":
            queue = self.select.single_attack()
        elif self.target ==  "multi":
            queue = self.select.multi_attack()
        elif self.target == "self":
            queue = self.select.self_attack(owner)
        
        return queue
    

    def init_select(self, queue : list):
        self.select = Selector(name=self.name,intent=self.intent,target=self.target,target_limit=self.targetLimit, queue=queue)
    

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
    def __init__(self,_id,_class,name,desc,target,targetLimit,intent,damage,cost,hits,dmgType):
        super().__init__(_id=_id, _class=_class, name=name, desc=desc,target=target,targetLimit=targetLimit,intent=intent,damage=damage,cost=cost,hits=hits,dmgType=dmgType)
    
    def doDamage(self, owner : Chara.Character, queue: list):

        self.init_select(queue)
        queue = self.check_target(owner)
        
        obj : Chara.Character = None

        i : dmgType.DamageType = None
        dmgList  = []

        for i in self.types:
            i.setAttack(owner)
            dmgList.append(i)    

        for obj in queue:
            for c in range(self.hits):
                obj.defend(dmgList)

        return True
        


class MagicalAttack(Attack):
    def __init__(self,_id,_class,name,desc,target,targetLimit,intent,damage,cost,hits,dmgType):
        super().__init__(_id=_id, _class=_class, name=name, desc=desc,target=target,targetLimit=targetLimit,intent=intent,damage=damage,cost=cost,hits=hits,dmgType=dmgType)
    
    def doDamage(self, owner : Chara.Character, queue: list):

        self.init_select(queue)
        queue = self.check_target(owner)


        obj : Chara.Character = None

        i : dmgType.DamageType = None
        dmgList  = []

        for i in self.types:
            i.setAttack(owner)
            dmgList.append(i)
        
        for obj in queue:
            for c in range(self.hits):
                obj.defend(dmgList)
            
        return True


class HealingAttack(Attack):
    def __init__(self,_id,_class,name,desc,target,targetLimit,intent,damage,cost,hits,dmgType):
        super().__init__(_id=_id, _class=_class, name=name, desc=desc,target=target,targetLimit=targetLimit,intent=intent,damage=damage,cost=cost,hits=hits,dmgType=dmgType)
    

    def doDamage(self, owner : Chara.Charactert, queue: list):
        self.init_select(queue)
        queue = self.check_target(owner)

        obj : Chara.Character = None


        i : dmgType.DamageType = None
        dmgList  = []

        for i in self.types:
            i.setAttack(owner)
            dmgList.append(i)


        for obj in queue:
            for c in range(self.hits):
                obj.healing(dmgList)

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
            hits = attacks_data[c]['hits'],
            dmgType = damagetypes)
        attacks_list.append(basicAttack)
    
    return attacks_list




def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)