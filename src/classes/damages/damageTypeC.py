from __future__ import annotations

import src.classes.entity_prototype as Chara
from helpers import check_if_attributes_exist



class DamageType:
    def __init__(self, file : str, name : str, desc : str, defType : str, min_atk: float, max_atk: float, min_heal: float, max_heal: float):
        self.file = file
        self.name = name
        self.main_element = self.name
        self.desc = desc
        self.defType = defType
        self.min_atk = min_atk
        self.max_atk = max_atk
        self.min_heal = min_heal
        self.max_heal = max_heal
        self.actived = True
        self.formula = ""
        self.atk = 0
    
    # No futuro implentar efeitos para certos tipos de dano
    def effect(self, owner : Chara.Character, target : Chara.Character ):
        pass

    def set_formula(self,owner_dmg,dmgA,final_dmg):
        #self.formula = f"[BASE:{self.base_atk}]+[OW:{owner_dmg}]+[{self.name}:{dmgA}]=[{self.base_atk + final_dmg}]"
        pass

    def set_attack(self, owner : Chara.Character):
        dmg_a = 0
        owner_dmg = 0


        if check_if_attributes_exist(owner):
            dmg_a = owner.attributes.elements[self.main_element]



        self.set_formula(owner_dmg,dmg_a,dmg_a)
        self.atk = self.max_atk + dmg_a

    def setHeal(self, owner : Chara.Character):
        pass
        












