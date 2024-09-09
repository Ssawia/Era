from __future__ import annotations
import uuid
#Provavelmente isso não é a melhor maneira de implementar várias classes, mas por enquanto vai dar certo, confia

import src.classes.attacks.attackC as Attacks
import src.classes.damages.damageTypeC as damageTypes
from src.classes.AIs import Ai
from math import trunc
import random
import helpers

import abstraction


class Status:
    def __init__(self, hp, hp_rgn, mp, mp_rgn, sp, sp_rgn, atk, atk_m, df, df_m, res, res_m, spd, crit, crit_max, dodge, item, sanity, load):
        self.hp = hp
        self.maxHp = self.hp
        self.regenHp = hp_rgn
        self.mp = mp
        self.maxMp = self.mp
        self.regenMp = mp_rgn
        self.sp = sp
        self.maxSp = self.sp
        self.regenSp = sp_rgn
        self.atk = atk
        self.atkM = atk_m
        self.df = df
        self.dfM = df_m
        self.res = res
        self.resM = res_m
        self.spd = spd
        self.crit = crit
        self.maxCrit = crit_max
        self.dodge = dodge
        self.item = item
        self.sanity = sanity
        self.maxSanity = self.sanity

        self.load = load
        self.bonus = []


class Potencial:
    def __init__(self, potential) -> None:
        self.vitality: float = potential["vitality"]
        self.constitution: float = potential["constitution"]
        self.strength: float  = potential["strength"]
        self.fortitude: float = potential["fortitude"]
        self.attunement: float = potential["attunement"]
        self.intelligence: float = potential["intelligence"]
        self.will: float = potential["will"]
        self.faith: float = potential["faith"]
        self.arcane: float = potential["arcane"]
        self.dexterity: float = potential["dexterity"]
        self.fortune: float = potential["fortune"]

        self.bonus = []




class Attributes:
    status: Status
    def __init__(self, data : dict):
        self.attributes = data['attributes']
        self.potential = data['potential']
        self.resistances = data['resistances']


        self.vitality: int = self.attributes["vitality"]
        self.constitution: int = self.attributes["constitution"]
        self.strength: int  = self.attributes["strength"]
        self.fortitude: int = self.attributes["fortitude"]
        self.attunement: int = self.attributes["attunement"]
        self.intelligence: int = self.attributes["intelligence"]
        self.will: int = self.attributes["will"]
        self.faith: int = self.attributes["faith"]
        self.arcane: int = self.attributes["arcane"]
        self.dexterity: int = self.attributes["dexterity"]
        self.fortune: int = self.attributes["fortune"]

        self.bonus = []


        self.potential: Potencial = Potencial(self.potential)
        self.init_status()

        self.resistancesBase : dict = self.resistances
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
                attr_multply = self.potential.fortitude
                attr_stats = self.fortitude
                res_base = self.status.res
            if element[key] == "Faith":
                attr_multply = self.potential.faith
                attr_stats = self.faith
                res_base = self.status.resM
            if element[key] == "Arcane":
                attr_multply = self.potential.arcane
                attr_stats = self.arcane
                res_base = self.status.resM
            res = ((attr_stats * 10 * attr_multply) * resBase) + res_base
            resD[key] = trunc(res)
        
        self.resistances = resD

    def update_elements(self):
        res_d = {}
        elements = abstraction.get_elements("Atk")
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
                attr_multply = self.potential.strength
                attr_stats = self.strength
                atk_base = self.status.atk
            if element[key] == "Intelligence":
                attr_multply = self.potential.intelligence
                attr_stats = self.faith
                atk_base = self.status.atkM
            if element[key] == "Will":
                attr_multply = self.potential.will
                attr_stats = self.arcane
                atk_base = self.status.atkM


            res = (attr_stats * 10 * attr_multply) + atk_base
            res_d[key] = trunc(res)

        self.elements = res_d



    def init_status(self):
        #Vitality
        hp = trunc((self.vitality * 500 * self.potential.vitality) * 1)
        load = trunc((self.vitality * 10 * self.potential.vitality) * .5)
        #Constitution
        res = trunc((self.constitution * 5 * self.potential.constitution) * 1)
        hp_regen = trunc(((hp * .01) * self.constitution * self.potential.constitution) * .1)
        #Strength
        atk = trunc((self.strength * 20 * self.potential.strength) * 1)
        #Fortitude
        df = trunc(((self.fortitude + (self.strength * .5 * self.potential.strength)) * 10 * self.potential.fortitude) * 1)
        sp = trunc((self.fortitude * 100 * self.potential.fortitude) * .5)
        sp_regen = trunc(((sp * .01) * self.fortitude * self.potential.constitution) * .1)
        #Attunement
        mp = trunc((self.attunement * 100 * self.potential.attunement) * 1)
        #Intelligence
        atk_m = trunc(((self.intelligence + (self.arcane * .5 * self.potential.arcane)) * 10 * self.potential.intelligence) * 1)
        df_m = trunc(((self.intelligence + (self.faith * .5 * self.potential.faith)) * 10 * self.potential.intelligence) * .5)
        #Will
        res_m = trunc((self.will * 5 * self.potential.will) * 1)
        mp_regen = trunc(((mp * .01) * self.will * self.potential.will) * .1)
        sanity = trunc((self.will * 10 * self.potential.will) * .5)
        #faith - voltar depois para adicionar os elementos
        #arcane
        #dexterity
        spd = trunc((self.dexterity * 10 * self.potential.dexterity) * 1)
        dodge = trunc(((self.dexterity + (self.fortune * .5 * self.potential.fortune)) * 10 * self.potential.dexterity) * .5)
        max_crit = 200 + (self.dexterity * self.potential.dexterity)
        #fortune
        crit = ((self.fortune + (self.arcane * .5 * self.potential.arcane)) * .5 * self.potential.fortune) * .5
        item = trunc(((self.fortune + (self.faith * 10 * self.potential.faith)) * .1 * self.potential.fortitude) * .5)

        self.status: Status = Status(hp,hp_regen,mp,mp_regen,sp,sp_regen,atk,atk_m,df,df_m,res,res_m,spd,crit,max_crit,dodge,item,sanity, load)

    def update_status(self):
        pass




class Character:
    attacks: list[Attacks.Attack]


    def __init__(self, data_chara, _type : str, attributes : Attributes):

        self._id = data_chara['_id']
        self.uuid = uuid.uuid4()

        self.name = data_chara['name']
        self.gender = data_chara['gender']
        self.age = data_chara['age']
        self.nick = data_chara['nick']
        self.desc = data_chara['desc']

        self.lines: dict[str,list] = data_chara['lines']

        self.alive = True

        self.ai : Ai = Ai("attack_all",self.uuid,_type)

        self.attributes: Attributes  = attributes

        self.ids_attacks: list[int] = data_chara['attacks']
        self.get_attacks()

        self.effects = []

        print(f"[{self.name}]-->[{self.uuid}]")



    def get_status(self,index: int):
        try:
            #Literal muito burro pra usar lambda
            if self.alive:
                alive = "Alive"
            else:
                alive = "Dead"

            print(f"[{index}][{self.ai.typeAi}][{self.name}][{alive}] HP: {self.attributes.status.hp}/{self.attributes.status.maxHp} MP: {self.attributes.status.mp}/{self.attributes.status.maxMp} SPD: {self.attributes.status.spd}")
            return True
        except Exception as E:
            print(E)
            return False

    def get_info_attacks(self):
        attack : Attacks.Attack
        for attack in self.attacks:
            print(F"[A] {attack.name} | Target: {attack.target}/{attack.targetLimit} Intent: {attack.intent} Damages:")


    def get_attacks(self):
        attack : Attacks.Attack
        self.attacks = abstraction.getAttackClass(self.ids_attacks)
        for attack in self.attacks:
            attack.setDamages(owner=self)



    def is_alive(self):
        if self.attributes.status.hp <= 0:
            self.alive = False
            self.attributes.status.hp = 0
            helpers.say_line(self,"incapacitated")
            print(f"{self.name} died.")
        else:
            return True


    def defend(self, attack_name, damages_type : list, owner : Character, target : Character, crit : bool):
        self.is_alive()
        dmgType: damageTypes.DamageType
        df = 0
        total_dmg = 0
        types = '|'
        if self.alive:
            # Uma bela maneira de spammar o cli, favor consertar depois
            for dmgType in damages_type:

                    if crit:
                        print("[+][Crit] foi ativo")
                        crit_dmg = owner.attributes.status.maxCrit
                        crit_dmg = crit_dmg / 100
                    else:
                        crit_dmg = 1


                    #Uma merda, vou arrumar depois
                    if dmgType.file == "Physical":
                        df = trunc(self.attributes.status.df * .1)
                    elif dmgType.file == "Magical":
                        df = trunc(self.attributes.status.dfM * .1)


                    dmgType.effect(owner, target)
                    res = self.attributes.resistances[dmgType.defType]
                    dmg = dmgType.atk * crit_dmg
                    dmg = trunc(dmg -res - df)


                    self.attributes.status.hp -= dmg
                    total_dmg += dmg
                    types += f'{dmgType.name}({dmg})|'
                    
                    
                    #print(f"{self.name} tomou {dmgType.formula}*[{crit_dmg}]-[{ty}:{df}]-[RES:{res}]=[{dmg}] de dano do tipo {dmgType.defType}")
                    
            
            print(f"{owner.name} used {attack_name} and dealt {total_dmg} {types} damage to {self.name}")
            if helpers.check_line('damage',self.lines):
                line = random.choice(self.lines['damage'])
                print(f"{self.name}: {line}")
            self.is_alive()

        else:
            self.attributes.status.hp = 0
    

    def healing(self,damage_types : list):
        
        dmgType : damageTypes.DamageType
        
        if self.is_alive:
            
            for dmgType in damage_types:
                
                if self.attributes.status.hp + dmgType.heal < self.attributes.status.maxHp:
                    print(f"[{self.name}][HP:{self.attributes.status.hp}/{self.attributes.status.maxHp}] curou {dmgType.heal} e ficou com {self.attributes.status.hp + dmgType.heal} de vida")
                    self.attributes.status.hp += dmgType.heal
                else:
                    print(f"[{self.name}][HP:{self.attributes.status.hp}/{self.attributes.status.maxHp}] curou {dmgType.heal} e ficou com {self.attributes.status.hp} de vida")
        else:
            print("Já está morto, não tem como curar")











