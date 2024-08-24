from __future__ import annotations
import uuid
#Provavelmente isso não é a melhor maneira de implementar varias classes, mas por enquanto vai dar certo, confia

import src.classes.attacks.attackC as Attacks
import src.classes.damages.damageTypeC as damageTypes
from src.classes.AIs import Ai
from typing import List
from math import trunc

import abstraction


class Status:
    def __init__(self,hp,hpRgn,mp,mpRgn,sp,spRgn,atk,atkM,df,dfM,res,resM,spd,crit,critMax,dodge,item,sanity, load):
        self.hp = hp
        self.maxHp = self.hp
        self.regenHp = hpRgn
        self.mp = mp
        self.maxMp = self.mp
        self.regenMp = mpRgn
        self.sp = sp
        self.maxSp = self.sp
        self.regenSp = spRgn
        self.atk = atk
        self.atkM = atkM
        self.df = df
        self.dfM = dfM
        self.res = res
        self.resM = resM
        self.spd = spd
        self.crit = crit
        self.maxCrit = critMax
        self.dodge = dodge
        self.item = item
        self.sanity = sanity
        self.maxSanity = self.sanity

        self.load = load
        self.bonus = []
  

class Potencial:
    def __init__(self, potencial: dict) -> None:
        self.vitality: float = potencial["vitality"]
        self.constitution: float = potencial["constitution"]
        self.strength: float  = potencial["strength"]
        self.fortitude: float = potencial["fortitude"]
        self.attunement: float = potencial["attunement"]
        self.intelligence: float = potencial["intelligence"]
        self.will: float = potencial["will"]
        self.faith: float = potencial["faith"]
        self.arcane: float = potencial["arcane"]
        self.dexterity: float = potencial["dexterity"]
        self.fortune: float = potencial["fortune"]

        self.bonus = []




class Attributes:
    def __init__(self, attributes : dict, potencial: dict, resistances: dict):
        self.vitality: int = attributes["vitality"]
        self.constitution: int = attributes["constitution"]
        self.strength: int  = attributes["strength"]
        self.fortitude: int = attributes["fortitude"]
        self.attunement: int = attributes["attunement"]
        self.intelligence: int = attributes["intelligence"]
        self.will: int = attributes["will"]
        self.faith: int = attributes["faith"]
        self.arcane: int = attributes["arcane"]
        self.dexterity: int = attributes["dexterity"]
        self.fortune: int = attributes["fortune"]

        self.bonus = []

        
        self.potencial: Potencial = Potencial(potencial)
        self.init_status()

        self.resistancesBase : dict = resistances
        self.resistances: dict = {}
        self.update_resistances()

        self.elements = {}
        self.update_elements()
    

    def update_resistances(self):
        resD = {}
        elements = abstraction.get_elements("Res")
        element : dict = {}
        keys = self.resistancesBase.keys()

        attr_stats = 0
        attr_multply = 0
        res_base = 0

        for element in elements:
            key = list(element.keys())[0]

            if key not in keys:

                resBase = 1
            else:
                resBase = self.resistancesBase[key]

            if element[key] == "Fortitude":
                attr_multply = self.potencial.fortitude
                attr_stats = self.fortitude
                res_base = self.status.res
            if element[key] == "Faith":
                attr_multply = self.potencial.faith
                attr_stats = self.faith
                res_base = self.status.resM
            if element[key] == "Arcane":
                attr_multply = self.potencial.arcane
                attr_stats = self.arcane
                res_base = self.status.resM
            res = ((attr_stats * 10 * attr_multply) * resBase) + res_base
            resD[key] = trunc(res)
        
        self.resistances = resD
    
    def update_elements(self):
        resD = {}
        elements = abstraction.get_elements("Atk")
        element : dict = {}
        keys = self.resistancesBase.keys()

        attr_stats = 0
        attr_multply = 0
        atk_base = 0

        for element in elements:
            key = list(element.keys())[0]
            if key not in keys:
                resBase = 1

            #resBase = self.resistancesBase[key]
            if element[key] == "Strength":
                attr_multply = self.potencial.strength
                attr_stats = self.strength
                atk_base = self.status.atk
            if element[key] == "Intelligence":
                attr_multply = self.potencial.intelligence
                attr_stats = self.faith
                atk_base = self.status.atkM
            if element[key] == "Will":
                attr_multply = self.potencial.will
                attr_stats = self.arcane
                atk_base = self.status.atkM


            res = ((attr_stats * 10 * attr_multply)) + atk_base
            resD[key] = trunc(res)
        
        self.elements = resD
        

    
    def init_status(self):
        #Vitality
        hp = trunc((self.vitality * 100 * self.potencial.vitality) * 1)
        load = trunc((self.vitality * 10 * self.potencial.vitality) * .5)
        #Constitution
        res = trunc((self.constitution * 5 * self.potencial.constitution) * 1)
        hpRegen = trunc(((hp * .01) * self.constitution * self.potencial.constitution) * .1)
        #Strength
        atk = trunc((self.strength * 10 * self.potencial.strength) * 1)
        #Fortitude
        df = trunc(((self.fortitude + (self.strength * .5 * self.potencial.strength)) * 10 * self.potencial.fortitude) * 1)
        sp = trunc((self.fortitude * 100 * self.potencial.fortitude) * .5)
        spRegen = trunc(((sp * .01) * self.fortitude * self.potencial.constitution) * .1)
        #Attunement
        mp = trunc((self.attunement * 100 * self.potencial.attunement) * 1)
        #Intelligence
        atkM = trunc(((self.intelligence + (self.arcane * .5 * self.potencial.arcane)) * 10 * self.potencial.intelligence) * 1)
        dfM = trunc(((self.intelligence  + (self.faith * .5 * self.potencial.faith))* 10 * self.potencial.intelligence) * .5)
        #Will
        resM = trunc((self.will * 5 * self.potencial.will) * 1)
        mpRegen = trunc(((mp * .01) * self.will * self.potencial.will) * .1)
        sanity = trunc((self.will * 10 * self.potencial.will) * .5)
        #faith - voltar depois para adiconar os elementos
        item = (self.faith * 5 * self.potencial.faith) * .5
        #arcane
        #dexterity
        spd = trunc((self.dexterity * 10 * self.potencial.dexterity) * 1)
        dodge = trunc(((self.dexterity + (self.fortune * .5 * self.potencial.fortune)) * 10 * self.potencial.dexterity) * .5)
        maxCrit = 200 + (self.dexterity * self.potencial.dexterity)
        #fortune
        crit = ((self.fortune + (self.arcane * .5 * self.potencial.arcane)) * .5 * self.potencial.fortune) * .5
        item = trunc(((self.fortune + (self.faith * 10 * self.potencial.faith)) * .1 * self.potencial.fortitude) * .5)

        self.status: Status = Status(hp,hpRegen,mp,mpRegen,sp,spRegen,atk,atkM,df,dfM,res,resM,spd,crit,maxCrit,dodge,item,sanity, load)

    def update_status(self):
        pass  




class Character:
    def __init__(self, _id : int, data : dict, _type : str):
        data = next((sub for sub in data if sub['_id'] == _id))

        self._id = data['_id']
        self.uuid = uuid.uuid4()

        self.name = data['name']
        self.nick = data['nick']
        self.alive = True

        self.ai : Ai = Ai("attack_all",self.uuid,_type)

        self.attributes : Attributes = Attributes(data["attributes"], data["potencial"], data['resistances'])
        self.attacks: List[Attacks.Attack] = data['attacks']
        self.getAttacks()

        self.effects = []

        print(f"[{self.name}]-->[{self.uuid}]")

    

    def get_status(self):
        try:
            #Literal muito burro pra usar lambda
            if self.alive:
                alive = "Alive"
            else:
                alive = "Dead"

            print(f"[{self.name}][{alive}] HP: {self.attributes.status.hp}/{self.attributes.status.maxHp} MP: {self.attributes.status.mp}/{self.attributes.status.maxMp}")
            return True
        except Exception as E:
            return False
    
    def get_attacks(self):
        attack : Attacks.Attack
        for attack in self.attacks:
            print(F"[A] {attack.name} | Target: {attack.target}/{attack.targetLimit} Intent: {attack.intent} Damages:")


    def getAttacks(self):
        attack : Attacks.Attack
        self.attacks = abstraction.getAttackClass(self.attacks)
        for attack in self.attacks:
            attack.setDamages(owner=self)



    def isAlive(self):
        if self.attributes.status.hp <= 0:
            self.alive = False
            self.attributes.status.hp = 0
        else:
            return True


    def defend(self, damagesType : list, owner : Character, target : Character, crit : bool):
        self.isAlive()
        dmgType : damageTypes.DamageType
        df = 0
        ty = ''
        if self.alive:
            # Uma bela maneira de spammar o cli, favor consertar depois
            for dmgType in damagesType:
                    
                    if crit:
                        print("[+][Crit] foi ativo")
                        crit_dmg = owner.attributes.status.maxCrit
                        crit_dmg = crit_dmg / 100
                    else:
                        crit_dmg = 1


                    #Uma merda, vou arrumar depois
                    if dmgType.file == "Physical":
                        df = trunc(self.attributes.status.df * .1)
                        ty = 'PHY'
                    elif dmgType.file == "Magical":
                        df = trunc(self.attributes.status.dfM * .1)
                        ty = 'MAG'
                
                    dmgType.effect(owner, target)
                    res = self.attributes.resistances[dmgType.defType]
                    dmg = dmgType.atk * crit_dmg
                    dmg = dmg -res - (df)
                    self.attributes.status.hp -= dmg
                    self.isAlive()
                    print(f"{self.name} tomou {dmgType.formula}*[{crit_dmg}]-[{ty}:{df}]-[RES:{res}]=[{dmg}] de dano do tipo {dmgType.defType}")

        else:
            self.attributes.status.hp = 0
    

    def healing(self,damageTypes : list):
        
        dmgType : damageTypes.DamageType
        
        if self.isAlive:
            
            for dmgType in damageTypes:
                
                if self.attributes.status.hp + dmgType.heal < self.attributes.status.maxHp:
                    print(f"[{self.name}][HP:{self.attributes.status.hp}/{self.attributes.status.maxHp}] curou {dmgType.heal} e ficou com {self.attributes.status.hp + dmgType.heal} de vida")
                    self.attributes.status.hp += dmgType.heal
                else:
                    print(f"[{self.name}][HP:{self.attributes.status.hp}/{self.attributes.status.maxHp}] curou {dmgType.heal} e ficou com {self.attributes.status.hp} de vida")
        else:
            print("Já está morto, não tem como curar")











