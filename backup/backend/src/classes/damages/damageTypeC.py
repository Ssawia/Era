from __future__ import annotations

import src.classes.entity_prototype as Chara
from helpers import check_if_attributes_exist
import src.classes.effects.effect_class as Effect
from helpers import Log, log
import random



class DamageType:
    def __init__(self, file : str, name : str, desc : str, defType : str, min_atk: float, max_atk: float, min_heal: float, max_heal: float, effects: list[Effect]):
        self.file = file
        self.name = name
        self.main_element = self.name
        self.desc = desc
        self.defType = defType
        self.min_atk = min_atk
        self.max_atk = max_atk
        self.min_heal = min_heal
        self.max_heal = max_heal
        self.effects: list[Effect.Effect] = effects
        self.actived = True
        self.formula = ""
        self.atk = 0
    
    # No futuro implentar efeitos para certos tipos de dano
    def effect(self, owner : Chara.Character, target : Chara.Character, res_base: int):
        for effect in self.effects:
            num = random.randint(1,100)
            log(Log.INFO, f"{target.name} has {res_base}% to resist {effect.name}, roll = {num}", "[Battle][Effect]")
            if num > res_base:
                effect.active = True
                effect.has_temp = True
                effect.owner = target
                effect.giver = owner 
                log(Log.INFO, f"{effect.name} proc on {target.name}","[Battle][Effect]")
                effect.init_effect()
                target.effects_handler.add_effects([effect])
            else:
                log(Log.INFO, f"{target.name} resist to {effect.name}", "[Battle][Effect]")


    def setHeal(self, owner : Chara.Character):
        pass
        












