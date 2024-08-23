from __future__ import annotations

import classes.entitiesC as Chara
import classes.damages.damageTypeC as dmgType
import sys
import json
from abstraction import str_to_class
from typing import List
import uuid

# Depois de alguns minutos de filosofia, eu cheguei a conclusão que single e select é literalmente a mesma coisa, só muda o limite do ataque 🤡
# Vou deixar por enquanto, motivo ? preguiça

class Selector:
    def __init__(self,name : str , queue : list, target : str, target_limit : int, intent: str):
        self.attack_name = name
        self.queue = queue
        self.target = target
        self.target_limit = target_limit
        self.intent = intent
        self.listt: List[Chara.Character] = []
        

    
    def get_intent_on_queue(self, onEnemy : bool = False):
        chara : Chara.Character
        selected: List[Chara.Character] = []


        match self.intent:
            # Top 10 codigos fodas 2024
            case "help":
                for chara in self.queue:
                    if not onEnemy:
                        if chara.ai.typeAi == "Player":
                            selected.append(chara)
                    elif onEnemy:
                        if chara.ai.typeAi == "Enemy":
                            selected.append(chara)                       
                
            case "harm":
                for chara in self.queue:
                    if not onEnemy:
                        if chara.ai.typeAi == "Enemy":
                            selected.append(chara)
                    elif onEnemy:
                        if chara.ai.typeAi == "Player":
                            selected.append(chara)
                
            case "harmall":
                selected = self.queue
                
            case _:
                selected = self.queue

        self.listt = selected
    
    def remove_select(self):
        pass


    def select_in_queue(self):
        chara : Chara.Character
        self.get_intent_on_queue()
        selected = []
        idS = 0


       
        for c in range(self.target_limit):
            if len(self.listt) > 0:
                idL = 0
                print("==========================[Lista]==============================")
                for chara in self.listt:
                    print(f"[{idL}][{chara.name}] HP : {chara.attributes.status.hp}/{chara.attributes.status.maxHp}")
                    idL += 1

                msg = str(input("Selecione o ID: "))
                msg = int(msg)

                if msg <= len(self.listt) - 1:
                    selected.append(self.listt[msg])
                    self.listt.remove(self.listt[msg])

                print("==========================[Selecionados]==============================")
                for chara in selected:
                    
                    print(f"[{idS}][{chara.name}] HP : {chara.attributes.status.hp}/{chara.attributes.status.maxHp}")

                    idS += 1
                print("="*70)

        
        return selected
    

    def self_attack(self,owner):
        print(f"[{self.attack_name}][{self.intent}][{self.target}] Selecione {self.target_limit} alvo(s)")
        self.listt = []
        self.listt.append(owner)

        return self.listt

    def single_attack(self):
        print(f"[{self.attack_name}][{self.intent}][{self.target}] Selecione {self.target_limit} alvo(s)")
        return self.select_in_queue()

    def multi_attack(self):
        print(f"[{self.attack_name}][{self.intent}][{self.target}] Selecione {self.target_limit} alvo(s)")
        self.get_intent_on_queue()
        return self.listt
        

    def select_attack(self):
        print(f"[{self.attack_name}][{self.intent}][{self.target}] Selecione {self.target_limit} alvo(s)")
        return self.select_in_queue()

#Classe usada para definir o tipo de dano dos ataques, como ataque fisico ou ataque magico
class Attack:
    def __init__(self, _id : int, _class : str, name : str, desc : str, target : str, targetLimit : int, intent : str, damage : list, cost : dict ,hits : int, dmgType : list):
        self._id = _id
        self.uuid = uuid.uuid4()
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
        self.dmgList: List[dmgType.DamageType] = []
        self.select : Selector 
    
    def setDamages(self, owner : Chara.Character):
        i : dmgType.DamageType 

        for i in self.types:
            i.setAttack(owner)
            self.dmgList.append(i)

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
                if owner.attributes.status.mp >= self.cost[key]:
                    owner.attributes.status.mp -= self.cost[key]
                    canAttack = True
        

        return canAttack
                    
                

    
    def doDamage(self, owner : Chara.Character, queue: list, ai = False):
        pass

    def imwho(self):
       return self.name
    

        
       





