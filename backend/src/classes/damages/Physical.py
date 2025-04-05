import src.classes.entity.character as Chara
import src.classes.damages.damageTypeC as dmgType



class Slash(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType, effects):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType, effects=effects)

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque fisico"



class Strike(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType, effects):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType, effects=effects)


class Thrust(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType, effects):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType, effects=effects)

