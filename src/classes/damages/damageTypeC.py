from __future__ import annotations

import src.classes.entity_prototype as Chara
from helpers import check_if_attributes_exist



class DamageType:
    atk : float
    def __init__(self, file : str, name : str, desc : str, defType : str, base_atk : float = 0, heal : float = 0):
        self.file = file
        self.name = name
        self.main_element = self.name
        self.desc = desc
        self.defType = defType
        self.base_atk = base_atk
        self.heal = heal
        self.formula = ""
    
    # No futuro implentar efeitos para certos tipos de dano
    def effect(self, owner : Chara.Character, target : Chara.Character ):
        pass

    def set_formula(self,owner_dmg,dmgA,final_dmg):
        self.formula = f"[BASE:{self.base_atk}]+[OW:{owner_dmg}]+[{self.name}:{dmgA}]=[{self.base_atk + final_dmg}]"

    def set_attack(self, owner : Chara.Character):
        dmg_a = 0
        owner_dmg = 0
        base_damage = self.base_atk

        if check_if_attributes_exist(owner):
            dmg_a = owner.attributes.elements[self.main_element]
            owner_dmg = owner.attributes.status.atkM


        final_dmg = base_damage + dmg_a + owner_dmg
        self.set_formula(owner_dmg,dmg_a,final_dmg)
        self.atk = final_dmg

    def setHeal(self, owner : Chara.Character):
        pass
        












