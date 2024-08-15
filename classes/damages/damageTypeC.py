from __future__ import annotations
import sys
import classes.entitiesC as Chara
from typing import List



class DamageType:
    def __init__(self, name : str, desc : str, defType : str, atk : float = 0, heal : float = 0):
        self.name = name
        self.desc = desc
        self.defType = defType
        self.atk = atk
        self.heal = heal
        self.formula = ""
    
    # No futuro implentar efeitos para certos tipos de dano
    def effect(self, owner : Chara.Character, target : Chara.Character ):
        pass


    def setAttack(self,owner : Chara.Character):
        pass

    def setHeal(self, owner : Chara.Character):
        pass
        












