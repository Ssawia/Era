from __future__ import annotations
#Provavelmente isso não é a melhor maneira de implementar varias classes, mas por enquanto vai dar certo, confia

import classes.attacks.attackC as Attacks
import classes.damages.damageTypeC as damageTypes
from typing import List

import abstraction

class Status:
    def __init__(self,hp,hpRgn,mp,mpRgn,sp,spRgn,atk,atkM,df,dfM,res,resM,spd,crit,critMax,dodge,item,sanity, load, elements):
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
        self.elements : list = elements
  

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
        


class Attributes:
    def __init__(self, attributes : dict, potencial: dict):
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

        
        self.potencial: Potencial = Potencial(potencial)
        self.init_status()
    
    def init_status(self):
        #Vitality
        hp = (self.vitality * 100 * self.potencial.vitality) * 1
        load = (self.vitality * 10 * self.potencial.vitality) * .5
        #Constitution
        res = (self.constitution * 10 * self.potencial.constitution) * 1
        hpRegen = ((hp * .01) * self.constitution * self.potencial.constitution) * .5
        #Strength
        atk = (self.strength * 10 * self.potencial.strength) * 1
        #Fortitude
        df = ((self.fortitude + (self.strength * .5 * self.potencial.strength)) * 10 * self.potencial.fortitude) * 1
        sp = (self.fortitude * 100 * self.potencial.fortitude) * .5
        spRegen = ((sp * .01) * self.fortitude * self.potencial.constitution) * .5
        #Attunement
        mp = (self.attunement * 100 * self.potencial.attunement) * 1
        #Intelligence
        atkM = ((self.intelligence + (self.arcane * .5 * self.potencial.arcane)) * 10 * self.potencial.intelligence) * 1
        dfM = ((self.intelligence  + (self.faith * .5 * self.potencial.faith))* 10 * self.potencial.intelligence) * .5
        #Will
        resM = (self.will * 10 * self.potencial.will) * 1
        mpRegen = ((mp * .01) * self.will * self.potencial.will) * .5
        sanity = (self.will * 10 * self.potencial.will) * .5
        #faith - voltar depois para adiconar os elementos
        telesma = (self.faith * 10 * self.potencial.faith) * 1
        water = (self.faith * 10 * self.potencial.faith) * 1
        wind = (self.faith * 10 * self.potencial.faith) * 1
        earth = (self.faith * 10 * self.potencial.faith) * 1
        fire = (self.faith * 10 * self.potencial.faith) * 1
        item = (self.faith * 5 * self.potencial.faith) * .5
        #arcane
        profane = (self.arcane * 10 * self.potencial.arcane) * 1
        poison = (self.arcane * 10 * self.potencial.arcane) * 1
        blood = (self.arcane * 10 * self.potencial.arcane) * 1
        control = (self.arcane * 10 * self.potencial.arcane) * 1
        insanity = (self.arcane * 10 * self.potencial.arcane) * 1
        #dexterity
        spd = (self.dexterity * 10 * self.potencial.dexterity) * 1
        dodge = ((self.dexterity + (self.fortune * .5 * self.potencial.fortune)) * 10 * self.potencial.dexterity) * .5
        maxCrit = 100 + (self.dexterity * .1 * self.potencial.dexterity)
        #fortune
        crit = ((self.fortune + (self.arcane * .5 * self.potencial.arcane)) * .01 * self.potencial.fortune) * .5
        item = ((self.fortune + (self.faith * .5 * self.potencial.faith)) * .01 * self.potencial.fortitude) * .5

        elements = {
            "Telesma": telesma, 
            "Water": water, 
            "Wind": wind, 
            "Earth": earth, 
            "Fire": fire,

            "Profane": profane,
            "Poison": poison,
            "Blood": blood,
            "Control": control,
            "Insanity": insanity,
        }

        self.status: Status = Status(hp,hpRegen,mp,mpRegen,sp,spRegen,atk,atkM,df,dfM,res,resM,spd,crit,maxCrit,dodge,item,sanity, load, elements)

    def update_status(self):
        pass  


class Character:
    def __init__(self, _id : int, data : dict, _type : str):
        data = next((sub for sub in data if sub['_id'] == _id))

        self._id = data['_id']
        self.name = data['name']
        self.nick = data['nick']
        self.type = _type
        self.alive = True

        self.attributes : Attributes = Attributes(data["attributes"], data["potencial"])
        self.attacks: List[Attacks.Attack] = data['attacks']
        self.getAttacks()

    

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


    def defend(self, damagesType : list):
        self.isAlive()
        dmgType : damageTypes.DamageType
        if self.alive:
            # Uma bela maneira de spammar o cli, favor consertar depois
            for dmgType in damagesType:
                if dmgType.defType == "PhysicalDamage":
                    dmg = dmgType.atk - self.attributes.status.df
                    self.attributes.status.hp -= dmg
                    self.isAlive()
                    print(f"{self.name} tomou {dmgType.atk}-{self.attributes.status.df}={dmg} de dano")
                elif dmgType.defType == "MagicalDamage":
                    dmg = dmgType.atk - self.attributes.status.dfM
                    self.attributes.status.hp -= dmg
                    self.isAlive()
                    print(f"{self.name} tomou {dmgType.atk}-{self.attributes.status.dfM}={dmg} de dano")
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











