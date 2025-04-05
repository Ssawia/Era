
from __future__ import annotations
import src.classes.temps.temp_class_handler as th
import src.classes.entity.character as ch
import src.classes.entity.potencial as pt
import src.classes.entity.status as st
import uuid
import helpers
import abstraction
import helpers
from math import trunc


class Attributes:
    def __init__(self, data : dict, parent = None):
        self.uid =  uuid.uuid4()
        self._parent: ch.Character | None = parent

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
        self.temp_handler: th.TempHandler = th.TempHandler(self,self._parent.name)

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
        self.update_attributes()

        self.bonus = []

        self.potential: pt.Potencial = pt.Potencial(self.potential)
        self.attributes_bonus = {}
        self.update_attributes_bonus()
        
        self.status: st.Status | None = None
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
        helpers.log(helpers.Log.DEBUG, "Updating Attributes", f"[{self._parent.name}][Attributes]")

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



    def add_xp(self,amount: float, owner: ch.Character):

        if amount > 0:
            self.xp += amount
            if self.xp >= self.max_xp:
                self.level_up(owner)
                self.rest_xp = self.xp - self.max_xp
                self.xp = 0
                self.max_xp = trunc(self.max_xp * 1.069)
                self.add_xp(self.rest_xp,owner)


    def level_up(self,owner: ch.Character):
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
    

    def update_status(self, in_battle = False, rest_hp = 0, rest_mp = 0, rest_sp = 0):

        helpers.log(helpers.Log.DEBUG, "Updating Status",  f"[{self._parent.name}][Attributes][Status]")

        #Physical Status

            #Vitality
        hp = trunc(((100 + (5 * self.attributes_bonus['vitality'])) + self.temp_handler.get_add_bonus("hp","add")) * self.temp_handler.get_mult_bonus("hp","mult")) - rest_hp
        hp_regen = trunc((hp / 3) + self.temp_handler.get_add_bonus("hp_regen","add")) * self.temp_handler.get_mult_bonus("hp_regen","mult")

            #Fortitude
        df = trunc((self.attributes_bonus['fortitude']) + self.temp_handler.get_add_bonus("df","add")) * self.temp_handler.get_mult_bonus("df","mult")


            #Constitution
        sp = trunc((100 + (5 * self.attributes_bonus['constitution'])) + self.temp_handler.get_add_bonus("sp","add")) * self.temp_handler.get_mult_bonus("sp","mult") - rest_sp
        sp_regen = trunc((sp / 3) + self.temp_handler.get_add_bonus("sp_regen","add")) * self.temp_handler.get_mult_bonus("sp_regen","mult")
        res = trunc((10 + (self.attributes_bonus['constitution'] + self.attributes_bonus['will']) / 2) + self.temp_handler.get_add_bonus("res","add")) * self.temp_handler.get_mult_bonus("res","mult")

        
            #Strength
        atk = trunc(self.attributes_bonus['strength'] + self.temp_handler.get_add_bonus("atk","add")) * self.temp_handler.get_mult_bonus("atk","mult")
        load = trunc((10 * self.attributes_bonus['strength']) + self.temp_handler.get_add_bonus("load","add")) * self.temp_handler.get_mult_bonus("load","mult")

        #Magical Status


            #Intelligence
        if (self.faith * self.potential.faith) >= (self.arcane * self.potential.arcane):
            atk_m = trunc(((self.attributes_bonus['intelligence'] + ((self.potential.intelligence + self.potential.faith) / 2)) + self.temp_handler.get_add_bonus("atk_m","add"))) * self.temp_handler.get_mult_bonus("atk_m","mult")
            df_m = trunc((self.attributes_bonus['intelligence'] + ((self.potential.intelligence + self.potential.faith) / 2)) + self.temp_handler.get_add_bonus("df_m","add")) * self.temp_handler.get_mult_bonus("df_m","mult")
        else:
            atk_m = trunc((self.attributes_bonus['intelligence'] + ((self.potential.intelligence + self.potential.arcane) / 2) + self.temp_handler.get_add_bonus("atk_m","add"))) * self.temp_handler.get_mult_bonus("atk_m","mult")
            df_m = trunc((self.attributes_bonus['intelligence'] + ((self.potential.intelligence + self.potential.arcane) / 2)) + self.temp_handler.get_add_bonus("df_m","add")) * self.temp_handler.get_mult_bonus("df_m","mult")

        res_m = trunc((10 + (self.attributes_bonus['intelligence'] + self.attributes_bonus['will']) / 2) + self.temp_handler.get_add_bonus("res_m","add")) * self.temp_handler.get_mult_bonus("res_m","mult")


            #Attunement
        mp = trunc((100 + (5 * self.attributes_bonus['attunement'])) + self.temp_handler.get_add_bonus("mp","add")) * self.temp_handler.get_mult_bonus("mp","mult") - rest_mp
        mp_regen = trunc((mp / 3) + self.temp_handler.get_add_bonus("mp_regen","add")) * self.temp_handler.get_mult_bonus("mp_regen","mult")


        
        

        #Special Attributes

            #fortune
        crit = trunc(self.attributes_bonus['fortune'] + self.temp_handler.get_add_bonus("crit","add")) * self.temp_handler.get_mult_bonus("crit","mult")
        
            #dexterity
        max_crit = trunc(self.attributes_bonus['dexterity'] + self.temp_handler.get_add_bonus("max_crit","add")) * self.temp_handler.get_mult_bonus("max_crit","mult")
        min_spd = trunc(1 + self.attributes_bonus['dexterity'])
        max_spd = trunc(10 + self.attributes_bonus['dexterity'])
        spd = [min_spd,max_spd]

            #Will
        sanity = trunc(((100 + self.attributes_bonus['will']) + self.temp_handler.get_add_bonus("sanity","add")) * self.temp_handler.get_mult_bonus("sanity","mult"))
        
        
        
        #Pra tirar
        dodge = 0
        item = 0

        if self.status != None:
            if in_battle:
                rest_hp = self.status.maxHp - self.status.hp
                rest_mp = self.status.maxMp - self.status.mp
                rest_sp = self.status.maxSp - self.status.sp
            
            self.status.hp = hp - rest_hp
            self.status.maxHp = self.status.hp + rest_hp
            self.status.regenHp = hp_regen
            self.status.sp = sp - rest_sp
            self.status.maxSp = self.status.sp + rest_sp
            self.status.regenSp = sp_regen
            self.status.mp = mp - rest_mp
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
            self.status.crit = crit
            self.status.maxCrit = max_crit
            self.status.load = load

        else:
            self.status: st.Status = st.Status(hp,hp_regen,mp,mp_regen,sp,sp_regen,atk,atk_m,df,df_m,res,res_m,spd,crit,max_crit,sanity, load)
            self.update_status(in_battle)