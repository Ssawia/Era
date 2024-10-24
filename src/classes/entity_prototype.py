from __future__ import annotations
from src.classes.effects.effect_handler_class_prototype import EffectHandler
from src.classes.ia_class_prototype import Ai
from math import trunc
from dataclasses import dataclass
import uuid
import random
import helpers
from helpers import log,Log
import abstraction
import src.classes.damages.damageTypeC as damageTypes
import src.classes.attacks.attackC as Attacks
from src.classes.temp.temp_class_handler import TempHandler, Temp







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


    def get_info_dict(self):

        data = {
            "status": {
                "hp": self.hp,
                "max_hp": self.maxHp,
                "regen_hp": self.regenHp,
                "mp": self.mp,
                "max_mp": self.maxMp,
                "regen_mp": self.regenMp,
                "sp": self.sp,
                "max_sp": self.maxSp,
                "regen_sp": self.regenSp,
                "atk": self.atk,
                "atk_m": self.atkM,
                "df": self.df,
                "df_m": self.dfM,
                "res": self.res,
                "res_m": self.resM,
                "spd": self.spd,
                "crit": self.crit,
                "max_crit": self.maxCrit,
                "dodge": self.dodge,
                "item": self.item,
                "sanity": self.sanity,
                "max_sanity": self.maxSanity,
                "load": self.load
            }
        }



        return data


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
    vitality: int = 0
    constitution: int = 0
    strength: int = 0
    fortitude: int = 0
    attunement: int = 0
    intelligence: int = 0
    will: int = 0
    faith: int = 0
    arcane: int = 0
    dexterity: int = 0
    fortune: int = 0
    def __init__(self, data : dict, parent = None):
        self.uid =  uuid.uuid4()
        self._parent: Character | None = parent

        self.attributes = data['attributes']
        self.potential = data['potential']
        self.resistances = data['resistances']

        self.level = 1
        self.max_level = 100

        self.xp = 0
        self.max_xp = 100
        self.rest_xp = 0


        self._vitality: int = self.attributes["vitality"]
        self._constitution: int = self.attributes["constitution"]
        self._strength: int  = self.attributes["strength"]
        self._fortitude: int = self.attributes["fortitude"]
        self._attunement: int = self.attributes["attunement"]
        self._intelligence: int = self.attributes["intelligence"]
        self._will: int = self.attributes["will"]
        self._faith: int = self.attributes["faith"]
        self._arcane: int = self.attributes["arcane"]
        self._dexterity: int = self.attributes["dexterity"]
        self._fortune: int = self.attributes["fortune"]



        self.vitality = self._vitality
        self.constitution = self._constitution
        self.strength = self._strength
        self.fortitude = self._fortitude
        self.attunement = self._attunement
        self.intelligence = self._intelligence
        self.will = self._will
        self.arcane = self._arcane
        self.dexterity = self._dexterity
        self.fortune = self._fortune



        self.bonus = []

        self.potential: Potencial = Potencial(self.potential)
        self.temp_handler: TempHandler = TempHandler(self,self._parent.name)
        self.init_status()


        self.resistancesBase : dict = self.resistances
        self.resistances: dict = {}
        self.update_resistances()

        self.elements = {}
        self.update_elements()


    def get_all_attr(self) -> dict[str,dict[str,list]]:



        data = {
            "attributes": {
                "vitality": ["Vitality",self.vitality,helpers.get_potencial_string(self.potential.vitality) ,self.temp_handler.get_add_bonus("vitality","add"), self.temp_handler.get_mult_bonus("vitality","mult")],
                "constitution": ["Constitution",self.constitution, helpers.get_potencial_string(self.potential.constitution), self.temp_handler.get_add_bonus("constitution", "add"), self.temp_handler.get_mult_bonus("constitution", "mult")],
                "fortitude": ["Fortitude",self.fortitude, helpers.get_potencial_string(self.potential.fortitude), self.temp_handler.get_add_bonus("fortitude", "add"), self.temp_handler.get_mult_bonus("fortitude", "mult")],
                "strength": ["Strength",self.strength, helpers.get_potencial_string(self.potential.strength), self.temp_handler.get_add_bonus("strength", "add"), self.temp_handler.get_mult_bonus("strength", "mult")],
                "attunement": ["Attunement",self.attunement, helpers.get_potencial_string(self.potential.attunement), self.temp_handler.get_add_bonus("attunement", "add"), self.temp_handler.get_mult_bonus("attunement", "mult")],
                "intelligence": ["Intelligence",self.intelligence, helpers.get_potencial_string(self.potential.intelligence), self.temp_handler.get_add_bonus("intelligence", "add"), self.temp_handler.get_mult_bonus("intelligence", "mult")],
                "will": ["Will",self.will, helpers.get_potencial_string(self.potential.will), self.temp_handler.get_add_bonus("will", "add"), self.temp_handler.get_mult_bonus("will", "mult")],
                "faith": ["Faith",self.faith, helpers.get_potencial_string(self.potential.faith), self.temp_handler.get_add_bonus("faith", "add"), self.temp_handler.get_mult_bonus("faith", "mult")],
                "arcane": ["Arcane",self.arcane, helpers.get_potencial_string(self.potential.arcane), self.temp_handler.get_add_bonus("arcane", "add"), self.temp_handler.get_mult_bonus("arcane", "mult")],
                "dexterity": ["Dexterity",self.dexterity, helpers.get_potencial_string(self.potential.dexterity), self.temp_handler.get_add_bonus("dexterity", "add"), self.temp_handler.get_mult_bonus("dexterity", "mult")],
                "fortune": ["Fortune",self.fortune, helpers.get_potencial_string(self.potential.fortune), self.temp_handler.get_add_bonus("fortune", "add"), self.temp_handler.get_mult_bonus("fortune", "mult")],

            }
        }


        return data


    def pos_init(self):
        self.update_attributes()


    def return_parent(self) -> any:
        return self._parent

    def update_attributes(self):
        log(Log.DEBUG, "Updating Attributes", f"[{self._parent.name}][Attributes]")

        self.vitality = trunc((self._vitality + self.temp_handler.get_add_bonus("vitality","add")) * self.temp_handler.get_mult_bonus("vitality","mult"))
        self.constitution = trunc((self._constitution + self.temp_handler.get_add_bonus("constitution","add")) * self.temp_handler.get_mult_bonus("constitution","mult"))
        self.fortitude = trunc((self._fortitude + self.temp_handler.get_add_bonus("fortitude","add")) * self.temp_handler.get_mult_bonus("fortitude","mult"))
        self.strength = trunc((self._strength + self.temp_handler.get_add_bonus("strength","add")) * self.temp_handler.get_mult_bonus("strength","mult"))
        self.attunement = trunc((self._attunement + self.temp_handler.get_add_bonus("attunement","add")) * self.temp_handler.get_mult_bonus("attunement","mult"))
        self.intelligence = trunc((self._intelligence + self.temp_handler.get_add_bonus("intelligence","add")) * self.temp_handler.get_mult_bonus("intelligence","mult"))
        self.will = trunc((self._will + self.temp_handler.get_add_bonus("will","add")) * self.temp_handler.get_mult_bonus("will","mult"))
        self.faith = trunc((self._faith + self.temp_handler.get_add_bonus("faith","add")) * self.temp_handler.get_mult_bonus("faith","mult"))
        self.arcane = trunc((self._arcane + self.temp_handler.get_add_bonus("arcane","add")) * self.temp_handler.get_mult_bonus("arcane","mult"))
        self.dexterity = trunc((self._dexterity + self.temp_handler.get_add_bonus("dexterity","add")) * self.temp_handler.get_mult_bonus("dexterity","mult"))
        self.fortune = trunc((self._fortune + self.temp_handler.get_add_bonus("fortune","add")) * self.temp_handler.get_mult_bonus("fortune","mult"))

        self.update_status(self._parent)



    def add_xp(self,amount: float, owner: Character):

        if amount > 0:
            self.xp += amount
            if self.xp >= self.max_xp:
                self.level_up(owner)
                self.rest_xp = self.xp - self.max_xp
                self.xp = 0
                self.max_xp = trunc(self.max_xp * 1.069)
                self.add_xp(self.rest_xp,owner)


    def level_up(self,owner: Character):
        if self.level + 1 <= 100:
            self.level += 1
            self._vitality += 1
            self._constitution += 1
            self._fortitude += 1
            self._strength += 1
            self._attunement += 1
            self._intelligence += 1
            self._will += 1
            self._faith += 1
            self._arcane += 1
            self._dexterity += 1
            self._fortune += 1

            self.update_attributes()
            self.update_status(owner)





    def update_resistances(self):
        resD = {}
        elements = abstraction.get_elements("Res")
        keys = self.resistancesBase.keys()
    

        attr_stats = 0
        attr_multply = 0
        res_base = 0

        for element in elements:
            key = list(element.keys())[0]

            if key not in keys:
                print(f"Resistence {key} does not exist.")
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

            res_key = key + "_Res"

            res = (((attr_stats * 10 * attr_multply) * resBase) + res_base + self.temp_handler.get_add_bonus(res_key,"add")) * self.temp_handler.get_mult_bonus(res_key,"mult")
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


            res = ((attr_stats * 10 * attr_multply) + atk_base + self.temp_handler.get_add_bonus(key,"add")) * self.temp_handler.get_mult_bonus(key,"mult")

            res_d[key] = trunc(res)

        self.elements = res_d




    def update_status(self,owner : Character):

        log(Log.DEBUG, "Updating Status",  f"[{self._parent.name}][Attributes][Status]")

        #Vitality
        hp = trunc(((self.vitality * 500 * self.potential.vitality) + self.temp_handler.get_add_bonus("hp","add")) * self.temp_handler.get_mult_bonus("hp","mult"))
        load = trunc(((self.vitality * 10 * self.potential.vitality) * .5) + self.temp_handler.get_add_bonus("load","add")) * self.temp_handler.get_mult_bonus("load","mult")
        #Constitution
        res = trunc((self.constitution * 5 * self.potential.constitution) + self.temp_handler.get_add_bonus("res","add")) * self.temp_handler.get_mult_bonus("res","mult")
        hp_regen = trunc((((hp * .01) * self.constitution * self.potential.constitution) * .1) + self.temp_handler.get_add_bonus("hp_regen","add")) * self.temp_handler.get_mult_bonus("hp_regen","mult")
        #Strength
        atk = trunc((self.strength * 20 * self.potential.strength) + self.temp_handler.get_add_bonus("atk","add")) * self.temp_handler.get_mult_bonus("atk","mult")
        #Fortitude
        df = trunc((self.fortitude + (self.strength * .5 * self.potential.strength) * 10 * self.potential.fortitude) + self.temp_handler.get_add_bonus("df","add")) * self.temp_handler.get_mult_bonus("df","mult")
        sp = trunc(((self.fortitude * 100 * self.potential.fortitude) * .5) + self.temp_handler.get_add_bonus("sp","add")) * self.temp_handler.get_mult_bonus("sp","mult")
        sp_regen = trunc((((sp * .01) * self.fortitude * self.potential.constitution) * .1) + self.temp_handler.get_add_bonus("sp_regen","add")) * self.temp_handler.get_mult_bonus("sp_regen","mult")
        #Attunement
        mp = trunc((self.attunement * 100 * self.potential.attunement) + self.temp_handler.get_add_bonus("mp","add")) * self.temp_handler.get_mult_bonus("mp","mult")
        #Intelligence
        atk_m = trunc((((self.intelligence + (self.arcane * .5 * self.potential.arcane)) * 10 * self.potential.intelligence) + self.temp_handler.get_add_bonus("atk_m","add"))) * self.temp_handler.get_mult_bonus("atk_m","mult")
        df_m = trunc((((self.intelligence + (self.faith * .5 * self.potential.faith)) * 10 * self.potential.intelligence) * .5) + self.temp_handler.get_add_bonus("df_m","add")) * self.temp_handler.get_mult_bonus("df_m","mult")
        #Will
        res_m = trunc((self.will * 5 * self.potential.will) + self.temp_handler.get_add_bonus("res_m","add")) * self.temp_handler.get_mult_bonus("res_m","mult")
        mp_regen = trunc((((mp * .01) * self.will * self.potential.will) * .1) + self.temp_handler.get_add_bonus("mp_regen","add")) * self.temp_handler.get_mult_bonus("mp_regen","mult")
        sanity = trunc(((self.will * 10 * self.potential.will) * .5) + self.temp_handler.get_add_bonus("sanity","add")) * self.temp_handler.get_mult_bonus("sanity","mult")
        #faith - voltar depois para adicionar os elementos
        #arcane
        #dexterity
        spd = trunc((self.dexterity * 10 * self.potential.dexterity) + self.temp_handler.get_add_bonus("spd","add")) * self.temp_handler.get_mult_bonus("spd","mult")
        dodge = trunc((((self.dexterity + (self.fortune * .5 * self.potential.fortune)) * 10 * self.potential.dexterity) * .5) + self.temp_handler.get_add_bonus("dodge","add")) * self.temp_handler.get_mult_bonus("dodge","mult")
        max_crit = (200 + (self.dexterity * self.potential.dexterity) + self.temp_handler.get_add_bonus("max_crit","add")) * self.temp_handler.get_mult_bonus("max_crit","mult")
        #fortune
        crit = (((self.fortune + (self.arcane * .01 * self.potential.arcane)) * .4 * self.potential.fortune) * .5 + self.temp_handler.get_add_bonus("crit","add")) * self.temp_handler.get_mult_bonus("crit","mult")
        item = trunc((((self.fortune + (self.faith * 10 * self.potential.faith)) * .1 * self.potential.fortitude) * .5) + self.temp_handler.get_add_bonus("item","add")) * self.temp_handler.get_mult_bonus("item","mult")



        self.status.hp = hp
        self.status.maxHp = self.status.hp
        self.status.regenHp = hp_regen

        self.status.sp = sp
        self.status.maxSp = self.status.sp
        self.status.regenSp = sp_regen

        self.status.mp = mp
        self.status.maxMp = self.status.mp
        self.status.regenMp = mp_regen

        self.status.sanity = sanity
        self.status.maxSanity = self.status.sanity

        self.status.atk = atk
        self.status.atkM = atk_m

        self.status.df = df
        self.status.dfM = df_m

        self.status.res = res
        self.status.resM = res_m

        self.status.spd = spd
        self.status.dodge = dodge

        self.status.crit = crit
        self.status.maxCrit = max_crit

        self.status.item = item
        self.status.load = load


        self.update_elements()
        self.update_resistances()
        owner.update_damage_attacks()



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
        crit = ((self.fortune + (self.arcane * .25 * self.potential.arcane)) * .5 * self.potential.fortune) * .5
        item = trunc(((self.fortune + (self.faith * 10 * self.potential.faith)) * .1 * self.potential.fortitude) * .5)

        self.status: Status = Status(hp,hp_regen,mp,mp_regen,sp,sp_regen,atk,atk_m,df,df_m,res,res_m,spd,crit,max_crit,dodge,item,sanity, load)





class Character:
    attacks: list[Attacks.Attack]


    def __init__(self, data_chara, _type : str):

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

        self.ids_attacks: list[int] = data_chara['attacks']

        self.attacks = abstraction.get_attack_class(self.ids_attacks)

        self.attributes: Attributes | None  = Attributes(data_chara,self)

        self.update_damage_attacks()

        self.abilities = []



        self.effects_handler: EffectHandler | None = EffectHandler(self)




        log(Log.DEBUG, f"[{self.name}]-->[{self.uuid}]", "[Character]")


    def check_abilities(self):
        for aby in self.abilities:
            if aby == "Phoenix Blessing" and aby not in self.attributes.temp_handler.flags:
                log(Log.DEBUG, f"{self.name} has the ability Phoenix Blessing")
                test = Temp("Fire","add",0,0,1000,True,False,False, "Phoenix Blessing")
                self.attributes.temp_handler.add_temp([test])

    def on_death_abylity(self):
        self.attributes.temp_handler.remove_temp(flags=self.abilities)




    def add_id_attacks(self, ids: list[int] | list[str]):

        for ida in ids:
            if ida not in self.ids_attacks:
                self.ids_attacks.append(ida)
            else:
                print("Attack ID already exist")

        self.get_attacks()

    def remove_id_attacks(self,ids: list[int]):
        for ida in ids:
            if ida in self.ids_attacks:
                self.ids_attacks.remove(ida)

        self.get_attacks()



    def get_status(self,index: int):

            #Literal muito burro pra usar lambda
        if self.alive:
            alive = "Alive"
        else:
            alive = "Dead"

        if self.attributes is not None:
            print(f"[{index}][{self.ai.typeAi}][{self.name}][{alive}] Level: {self.attributes.level} HP: {self.attributes.status.hp}/{self.attributes.status.maxHp} MP: {self.attributes.status.mp}/{self.attributes.status.maxMp} SPD: {self.attributes.status.spd}")
        else:
            print(f"[{index}][{self.ai.typeAi}][{self.name}][{alive}]")



    def get_info_attacks(self):
        attack : Attacks.Attack
        for attack in self.attacks:
            print(F"[A] {attack.name} | Target: {attack.target}/{attack.targetLimit} Intent: {attack.intent} Damages: {attack.get_total_dmg()}")


    def get_attacks(self):
        attack : Attacks.Attack
        print(self.ids_attacks)
        self.attacks = abstraction.get_attack_class(self.ids_attacks)
        self.update_damage_attacks()



    def update_damage_attacks(self):
        for attack in self.attacks:
            attack.set_damages(owner=self)



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
        
        if crit:
            print("[+][Crit] foi ativo")
            crit_dmg = owner.attributes.status.maxCrit
            crit_dmg = crit_dmg / 100
        else:
            crit_dmg = 1        


        if self.alive:
            # Uma bela maneira de spammar o cli, favor consertar depois
            for dmgType in damages_type:
                    #Uma merda, vou arrumar depois
                    if dmgType.file == "Physical":
                        df = trunc(self.attributes.status.df * .1)
                    elif dmgType.file == "Magical":
                        df = trunc(self.attributes.status.dfM * .1)


                    dmgType.effect(owner, target)
                    res = self.attributes.resistances[dmgType.defType]
                    dmg = dmgType.atk * crit_dmg
                    dmg = trunc(dmg -res - df)

                    if dmg <= 0:
                        dmg = 0


                    self.attributes.status.hp -= dmg
                    total_dmg += dmg
                    types += f'{dmgType.name}({dmg})|'
                    
                    
                    #print(f"{self.name} tomou {dmgType.formula}*[{crit_dmg}]-[{ty}:{df}]-[RES:{res}]=[{dmg}] de dano do tipo {dmgType.defType}")
                    

            log(Log.INFO, f"{owner.name} used {attack_name} and dealt {total_dmg} {types} damage to {self.name}")
            if helpers.check_line('damage',self.lines):
                line = random.choice(self.lines['damage'])
                log(Log.CHAT,line,f"[{self.name}]")

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











