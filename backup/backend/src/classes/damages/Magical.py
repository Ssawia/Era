import src.classes.entity_prototype as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.effects.effect_class as effect
import src.classes.temps.temp_class_handler as Temp
from helpers import Log, log
import abstraction
from src.classes.effects.ashen_curse import AshenCurse
import random

class Telesma(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal,defType, effects):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType, effects=effects)


class Fire(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType, effects):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType, effects=effects)



class Water(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType, effects):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType, effects=effects)
    

class Earth(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType, effects):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType, effects=effects)
    


class Wind(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType, effects):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType, effects=effects)
    

class Arcane(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType, effects):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType, effects=effects)
    

class Blood(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType, effects):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType, effects=effects)
    

class Poison(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType, effects):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType, effects=effects)


class Insanity(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType, effects):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType, effects=effects)

class Control(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType, effects):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType, effects=effects)
