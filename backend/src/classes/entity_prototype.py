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
from src.classes.attacks.attackC import Instance

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
    def __init__(self, data : dict, parent = None):
        self.uid =  uuid.uuid4()
        self._parent: Character | None = parent

        self.attributes = data['attributes']
        self.potential = data['potential']
        self.resistances = data['resistances']

        self.actions = data['actions']
        self.max_actions = self.actions

        self.level = 1
        self.max_level = 100

        self.xp = 0
        self.max_xp = 100
        self.rest_xp = 0

        self.battle_spd = 0


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
        self.attributes_bonus = {}
        self.update_attributes_bonus()
        self.temp_handler: TempHandler = TempHandler(self,self._parent.name)
        self.status: Status | None = None
        self.update_status()


        self.resistancesBase : dict = self.resistances
        self.resistances: dict = {}
        self.update_resistances()

        self.elements = {}
        self.update_elements()
    
    def update_attributes_bonus(self):
        self.attributes_bonus['vitality'] = self.potential.vitality * self.vitality
        self.attributes_bonus['constitution'] = self.potential.constitution * self.constitution
        self.attributes_bonus['fortitude'] = self.potential.fortitude * self.fortitude
        self.attributes_bonus['strength'] = self.potential.strength * self.strength
        self.attributes_bonus['intelligence'] = self.potential.intelligence * self.intelligence
        self.attributes_bonus["attunement"] = self.potential.intelligence * self.attunement
        self.attributes_bonus['will'] = self.potential.will * self.will
        self.attributes_bonus['faith'] = self.potential.faith * self.faith
        self.attributes_bonus['arcane'] = self.potential.arcane * self.arcane
        self.attributes_bonus['dexterity'] = self.potential.dexterity * self.dexterity
        self.attributes_bonus['fortune'] = self.potential.fortune * self.fortune


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

        self.vitality = trunc((self.vitality + self.temp_handler.get_add_bonus("vitality","add")) * self.temp_handler.get_mult_bonus("vitality","mult"))
        self.constitution = trunc((self.constitution + self.temp_handler.get_add_bonus("constitution","add")) * self.temp_handler.get_mult_bonus("constitution","mult"))
        self.fortitude = trunc((self.fortitude + self.temp_handler.get_add_bonus("fortitude","add")) * self.temp_handler.get_mult_bonus("fortitude","mult"))
        self.strength = trunc((self.strength + self.temp_handler.get_add_bonus("strength","add")) * self.temp_handler.get_mult_bonus("strength","mult"))
        self.attunement = trunc((self.attunement + self.temp_handler.get_add_bonus("attunement","add")) * self.temp_handler.get_mult_bonus("attunement","mult"))
        self.intelligence = trunc((self.intelligence + self.temp_handler.get_add_bonus("intelligence","add")) * self.temp_handler.get_mult_bonus("intelligence","mult"))
        self.will = trunc((self.will + self.temp_handler.get_add_bonus("will","add")) * self.temp_handler.get_mult_bonus("will","mult"))
        self.faith = trunc((self.faith + self.temp_handler.get_add_bonus("faith","add")) * self.temp_handler.get_mult_bonus("faith","mult"))
        self.arcane = trunc((self.arcane + self.temp_handler.get_add_bonus("arcane","add")) * self.temp_handler.get_mult_bonus("arcane","mult"))
        self.dexterity = trunc((self.dexterity + self.temp_handler.get_add_bonus("dexterity","add")) * self.temp_handler.get_mult_bonus("dexterity","mult"))
        self.fortune = trunc((self.fortune + self.temp_handler.get_add_bonus("fortune","add")) * self.temp_handler.get_mult_bonus("fortune","mult"))



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
            self.vitality += 1
            self.constitution += 1
            self.fortitude += 1
            self.strength += 1
            self.attunement += 1
            self.intelligence += 1
            self.will += 1
            self.faith += 1
            self.arcane += 1
            self.dexterity += 1
            self.fortune += 1

            self.update_attributes()
            self.update_status(owner)





    def update_resistances(self):
        resD = {}
        elements = abstraction.get_elements()
        keys = self.resistancesBase.keys()
    
        res_base = 0

        for element in elements:
            key = list(element.keys())[0]

            if key not in keys:
                print(f"Resistence {key} does not exist.")
                resBase = 1
            else:
                resBase = self.resistancesBase[key]

            res_key = key + "_Res"

            res = (resBase + res_base + self.temp_handler.get_add_bonus(res_key,"add")) * self.temp_handler.get_mult_bonus(res_key,"mult")
            resD[key] = res
        
        self.resistances = resD

    def update_elements(self):
        res_d = {}
        elements = abstraction.get_elements()
        attr_multply = 0
        for element in elements:
            key = list(element.keys())[0]
            
            if element[key] == "Strength":
                attr_multply =  self.attributes_bonus['strength']
            if element[key] == "Faith":
                attr_multply =  self.attributes_bonus['faith']
            if element[key] == "Arcane":
                attr_multply = self.attributes_bonus['arcane']
            if element[key] == "Intelligence":
                attr_multply = self.attributes_bonus['intelligence']
            if element[key] == "Will":
                attr_multply = self.attributes_bonus['will']

            res = (attr_multply + self.temp_handler.get_add_bonus(key,"add")) * self.temp_handler.get_mult_bonus(key,"mult")
            res_d[key] = trunc(res)

        self.elements = res_d
    

    def update_status(self, in_battle = False):

        log(Log.DEBUG, "Updating Status",  f"[{self._parent.name}][Attributes][Status]")
        rest_hp = 0
        rest_mp = 0
        rest_sp = 0


        hp = trunc(((self.vitality * 10 * self.potential.vitality) + self.temp_handler.get_add_bonus("hp","add")) * self.temp_handler.get_mult_bonus("hp","mult")) - rest_hp
        load = trunc(((self.vitality * 10 * self.potential.vitality) * .5) + self.temp_handler.get_add_bonus("load","add")) * self.temp_handler.get_mult_bonus("load","mult")
        #Vitality
        #Constitution
        res = 0
        hp_regen = trunc((((hp * .01) * self.constitution * self.potential.constitution) * .1) + self.temp_handler.get_add_bonus("hp_regen","add")) * self.temp_handler.get_mult_bonus("hp_regen","mult")
        #Strength
        atk = trunc(self.attributes_bonus['strength'] + self.temp_handler.get_add_bonus("atk","add")) * self.temp_handler.get_mult_bonus("atk","mult")
        
        crit = trunc(self.attributes_bonus['fortune'] + self.temp_handler.get_add_bonus("crit","add")) * self.temp_handler.get_mult_bonus("crit","mult")
        max_crit = trunc(self.attributes_bonus['dexterity'] + self.temp_handler.get_add_bonus("max_crit","add")) * self.temp_handler.get_mult_bonus("max_crit","mult")

        if (self.faith * self.potential.faith) >= (self.arcane * self.potential.arcane):
            atk_m = trunc(((self.intelligence * ((self.potential.intelligence + self.potential.faith) / 2)) + self.temp_handler.get_add_bonus("atk_m","add"))) * self.temp_handler.get_mult_bonus("atk_m","mult")
        else:
            atk_m = trunc(((self.intelligence * ((self.potential.intelligence + self.potential.arcane) / 2)) + self.temp_handler.get_add_bonus("atk_m","add"))) * self.temp_handler.get_mult_bonus("atk_m","mult")
        
        df = trunc((self.fortitude * self.potential.fortitude) + self.temp_handler.get_add_bonus("df","add")) * self.temp_handler.get_mult_bonus("df","mult")
        df_m = trunc(((self.intelligence * self.potential.intelligence)) + self.temp_handler.get_add_bonus("df_m","add")) * self.temp_handler.get_mult_bonus("df_m","mult")
        
        #Fortitude
        sp = trunc(((self.fortitude * 100 * self.potential.fortitude) * .5) + self.temp_handler.get_add_bonus("sp","add")) * self.temp_handler.get_mult_bonus("sp","mult") - rest_sp
        sp_regen = trunc((((sp * .01) * self.fortitude * self.potential.constitution) * .1) + self.temp_handler.get_add_bonus("sp_regen","add")) * self.temp_handler.get_mult_bonus("sp_regen","mult")
        #Attunement
        mp = trunc((self.attunement * 100 * self.potential.attunement) + self.temp_handler.get_add_bonus("mp","add")) * self.temp_handler.get_mult_bonus("mp","mult") - rest_mp
        #Intelligence
        #Will
        res_m = trunc((self.will * 5 * self.potential.will) + self.temp_handler.get_add_bonus("res_m","add")) * self.temp_handler.get_mult_bonus("res_m","mult")
        mp_regen = trunc((((mp * .01) * self.will * self.potential.will) * .1) + self.temp_handler.get_add_bonus("mp_regen","add")) * self.temp_handler.get_mult_bonus("mp_regen","mult")
        sanity = trunc(((self.will * 10 * self.potential.will) * .5) + self.temp_handler.get_add_bonus("sanity","add")) * self.temp_handler.get_mult_bonus("sanity","mult")
        #faith - voltar depois para adicionar os elementos
        #arcane
        #dexterity

        min_spd = trunc(1 + self.attributes_bonus['dexterity'])
        max_spd = trunc(10 + self.attributes_bonus['dexterity'])

        spd = [min_spd,max_spd]
        dodge = trunc((((self.dexterity + (self.fortune * .5 * self.potential.fortune)) * 10 * self.potential.dexterity) * .5) + self.temp_handler.get_add_bonus("dodge","add")) * self.temp_handler.get_mult_bonus("dodge","mult")
        #fortune
        item = trunc((((self.fortune + (self.faith * 10 * self.potential.faith)) * .1 * self.potential.fortitude) * .5) + self.temp_handler.get_add_bonus("item","add")) * self.temp_handler.get_mult_bonus("item","mult")
        

        if self.status != None:
            if in_battle:
                rest_hp = self.status.maxHp - self.status.hp
                rest_mp = self.status.maxMp - self.status.mp
                rest_sp = self.status.maxSp - self.status.sp
            
            
            self.status.hp = hp
            self.status.maxHp = self.status.hp + rest_hp
            self.status.regenHp = hp_regen
            self.status.sp = sp
            self.status.maxSp = self.status.sp + rest_sp
            self.status.regenSp = sp_regen
            self.status.mp = mp
            self.status.maxMp = self.status.mp + rest_mp
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

        else:
            self.status: Status = Status(hp,hp_regen,mp,mp_regen,sp,sp_regen,atk,atk_m,df,df_m,res,res_m,spd,crit,max_crit,dodge,item,sanity, load)
            self.update_status(in_battle)

        


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
        self.attack_slot: list[Instance] = []

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

    
    def update_instances(self):
        active_list = []
        log(Log.DEBUG, "Updating Instances in attack slot", f"[{self.name}]")
        for instance in self.attack_slot:
            if instance.active:
                active_list.append(instance)
            self.attack_slot = active_list




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
            print(f"[{index}][{self.ai.typeAi}][{self.name}][{alive}] Action: {self.attributes.actions} Level: {self.attributes.level} HP: {self.attributes.status.hp}/{self.attributes.status.maxHp} MP: {self.attributes.status.mp}/{self.attributes.status.maxMp} SPD: {self.attributes.status.spd}")
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
            return False
        else:
            return True
     
    def deal_damage(self,dmg_obj,damage_roll, damage_bonus, owner):
        self.is_alive()

        if self.alive:
            dmg_obj.effect(owner, self)
            res = self.attributes.resistances[dmg_obj.defType]
                    
            dmg_deal = (damage_roll + damage_bonus) * res 
            dmg_deal = trunc(dmg_deal)
            if dmg_deal <= 0:
                dmg_deal = 0

            old_hp = self.attributes.status.hp
            self.attributes.status.hp -= dmg_deal
            types = f'|{self.name} taken {dmg_obj.name}({damage_roll}+{damage_bonus})*({res})| = {dmg_deal} damage | {self.name} HP:{old_hp}>{self.attributes.status.hp}.'
            return types
        else:
            self.attributes.status.hp = 0


    def defend(self, attack_name, damages_type : list, owner : Character, target : Character):
        self.is_alive()
        dmgType: damageTypes.DamageType
        total_dmg = 0
        types = '|'
        

        if self.alive:
            # Uma bela maneira de spammar o cli, favor consertar depois
            for dmgType in damages_type:
                    min_atk = dmgType.min_atk
                    max_atk = dmgType.max_atk
                    crit = owner.attributes.status.crit
                    max_crit = owner.attributes.status.maxCrit
                    dmg_bonus = owner.attributes.elements[dmgType.main_element]


                    roll = random.randint(min_atk + crit,max_atk + max_crit)
                    log(Log.INFO, f"[{dmgType.main_element}]{min_atk}(+{crit})-{max_atk}(+{max_crit})={roll}+{dmg_bonus}")


                    dmgType.effect(owner, target)
                    res = self.attributes.resistances[dmgType.defType]
                
                    dmg = (roll + dmg_bonus) * res 
                    dmg = trunc(dmg)

                    if dmg <= 0:
                        dmg = 0


                    self.attributes.status.hp -= dmg
                    total_dmg += dmg
                    types += f'{dmgType.name}({roll}+{dmg_bonus})*({res})|'
                    
                    
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
                min_atk = dmgType.min_atk
                max_atk = dmgType.max_atk
                crit = self.attributes.status.crit
                max_crit = self.attributes.status.maxCrit
                dmg_bonus = self.attributes.elements[dmgType.main_element]

                min_roll = min_atk + crit
                max_roll = max_atk + max_crit

                if min_roll >= max_roll:
                    roll = min_roll
                else:
                    roll = random.randint(min_roll,max_roll)
        
                heal = roll + dmg_bonus

                if self.attributes.status.hp + heal < self.attributes.status.maxHp:
                    print(f"[{self.name}][HP:{self.attributes.status.hp}/{self.attributes.status.maxHp}] curou {heal} e ficou com {self.attributes.status.hp + heal} de vida")
                    self.attributes.status.hp += heal
                else:
                    print(f"[{self.name}][HP:{self.attributes.status.hp}/{self.attributes.status.maxHp}] curou {heal} e ficou com {self.attributes.status.hp} de vida")
        else:
            print("Já está morto, não tem como curar")








class Energy:
    def __init__(self,name,sig,value,max_value):
        self.name = name
        self.sig = sig
        self.value = value
        self.max_value = max_value








