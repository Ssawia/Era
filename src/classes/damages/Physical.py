import src.classes.entity_prototype as Chara
import src.classes.damages.damageTypeC as dmgType



class Slash(dmgType.DamageType):
    def __init__(self, file,name, desc, base_atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, base_atk=base_atk, heal=heal,defType=defType)

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque fisico"



class Strike(dmgType.DamageType):
    def __init__(self, file,name, desc, base_atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, base_atk=base_atk, heal=heal,defType=defType)


    def effect(self, owner : Chara.Character, target : Chara.Character ):
        return "Um ataque fisico"



class Thrust(dmgType.DamageType):
    def __init__(self, file,name, desc, base_atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, base_atk=base_atk, heal=heal,defType=defType)


    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque fisico"