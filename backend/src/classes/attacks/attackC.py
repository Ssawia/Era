# circular import eu te odeio
from __future__ import annotations
import src.classes.entity.character as Chara
import src.classes.damages.damageTypeC as dmg
from src.classes.events.event_class_prototype import On_Start_Attack


import uuid

# Depois de alguns minutos de filosofia, eu cheguei a conclusão que single e select é literalmente a mesma coisa, só muda o limite do ataque 🤡
# Vou deixar por enquanto, motivo ? preguiça

class Instance:

    def __init__(self, attack: Attack, queue: list[Chara.Character], active: bool, owner: bool):
        self.attack: Attack = attack 
        self.queue: list[Chara.Character] = queue
        self.exclusion_queue: list[Chara.Character] = []
        self.active: bool = active
        self.instance_target:Instance = None
        self.owner: Chara.Character = owner
    
    def check(self):
        if len(self.queue) == len(self.exclusion_queue):
            self.active = False

class Selector:
    def __init__(self,name : str , queue : list, target : str, target_limit : int, intent: str):
        self.attack_name = name
        self.queue = queue
        self.target = target
        self.target_limit = target_limit
        self.intent = intent
        self.listt: list[Chara.Character] = []
        

    
    def get_intent_on_queue(self, on_enemy : bool = False):
        chara : Chara.Character
        selected: list[Chara.Character] = []


        match self.intent:
            # Top 10 codigos fodas 2024
            case "help":
                for chara in self.queue:
                    if not on_enemy:
                        if chara.ai.typeAi == "Player":
                            selected.append(chara)
                    elif on_enemy:
                        if chara.ai.typeAi == "Enemy":
                            selected.append(chara)                       
                
            case "harm":
                for chara in self.queue:
                    if not on_enemy:
                        if chara.ai.typeAi == "Enemy":
                            selected.append(chara)
                    elif on_enemy:
                        if chara.ai.typeAi == "Player":
                            selected.append(chara)
                
            case "harmall":
                selected = self.queue
                
            case _:
                selected = self.queue


        self.listt = selected
    
    def remove_select(self):
        pass


    def select_in_queue(self, owner : Chara.Character):
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
        
        
        return selected
    

    def self_attack(self,owner):
        print(f"[{self.attack_name}][{self.intent}][{self.target}] Selecione {self.target_limit} alvo(s)")
        self.listt = []
        self.listt.append(owner)

        return self.listt

    def single_attack(self,owner):
        print(f"[{self.attack_name}][{self.intent}][{self.target}] Selecione {self.target_limit} alvo(s)")
        return self.select_in_queue(owner)

    def multi_attack(self,owner):
        print(f"[{self.attack_name}][{self.intent}][{self.target}] Selecione {self.target_limit} alvo(s)")
        self.get_intent_on_queue()
        return self.listt
        

    def select_attack(self,owner):
        print(f"[{self.attack_name}][{self.intent}][{self.target}] Selecione {self.target_limit} alvo(s)")
        return self.select_in_queue(owner)

#Classe usada para definir o tipo de dano dos ataques, como ataque fisico ou ataque magico
class Attack:
    

    def __init__(self, attack_data, dmg_type : list):
        self._id = attack_data['_id']
        self.uuid = uuid.uuid4()
        self.class_name = attack_data['className']
        self.file = attack_data['file']
        self.name = attack_data['name']
        self.def_name = attack_data['defName']
        self.main_element = attack_data['main_element']
        self.desc = attack_data['desc']
        self.line = attack_data['line']
        self.target = attack_data['target']
        self.targetLimit = attack_data['target-limit']
        self.intent = attack_data['intent']
        self.damage = attack_data['damage']
        self.cost = attack_data['cost']
        self.hits = attack_data['hits']
        self.types = dmg_type
        self.select: Selector | None = None
        self.dmgList: list[dmg.DamageType] = []

        self.queue = []
        self.battle_queue: list[list[Chara.Character]] = []
        self.owner: Chara.Character| None = None 
        self.ai: bool = False

    def set_damages(self, owner : Chara.Character):
        i : dmg.DamageType
        self.dmgList = []

        for i in self.types:
            self.dmgList.append(i)
    
    def backlash_damage(self):
        backlash_dmg = 0
        for dmg in self.dmgList:
            backlash_dmg += dmg.max_atk

        return backlash_dmg
    

    def choice_player(self):
        self.init_select(self.queue)
        return self.check_target(self.owner)

    def check_target(self, owner : Chara.Character):
        queue = []
        if self.target == "select":
            queue = self.select.select_attack(owner)
        elif self.target == "single":
            queue = self.select.single_attack(owner)
        elif self.target ==  "multi":
            queue = self.select.multi_attack(owner)
        elif self.target == "self":
            queue = self.select.self_attack(owner)
        
        
        return queue


    def get_total_dmg(self):
        dmg: dmg.DamageType
        total_dmg = 0

        for dmg in self.dmgList:
            total_dmg += dmg.atk

        return total_dmg
    

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
                    
    
    def onStart(self, owner: Chara.Character, target: Chara.Character):
        data = On_Start_Attack("on_attack_start", owner,target,self)
        return data


    def imwho(self):
       return self.name
    

        
       





