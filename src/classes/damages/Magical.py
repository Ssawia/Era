import src.classes.entitiesC as Chara
import src.classes.damages.damageTypeC as dmgType

import random

class Telesma(dmgType.DamageType):
    def __init__(self, file,name, desc, base_atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, base_atk=base_atk, heal=heal,defType=defType)
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"



class Fire(dmgType.DamageType):
    def __init__(self, file,name, desc, base_atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, base_atk=base_atk, heal=heal,defType=defType)


    def effect(self, owner : Chara.Character, target : Chara.Character):
        chance_to_burn = 25

        num = random.randint(1,100)
        if num <= chance_to_burn:
            print(f"{target.name} was burned alive")
            #target.alive = False




class Water(dmgType.DamageType):
    def __init__(self, file,name, desc, base_atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, base_atk=base_atk, heal=heal,defType=defType)
    

    def effect(self, owner : Chara.Character, target : Chara.Character):

        return "Um ataque magico"





class Earth(dmgType.DamageType):
    def __init__(self, file,name, desc, base_atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, base_atk=base_atk, heal=heal,defType=defType)
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"




class Wind(dmgType.DamageType):
    def __init__(self, file,name, desc, base_atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, base_atk=base_atk, heal=heal,defType=defType)
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"





class Arcane(dmgType.DamageType):
    def __init__(self, file,name, desc, base_atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, base_atk=base_atk, heal=heal,defType=defType)
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"




class Blood(dmgType.DamageType):
    def __init__(self, file,name, desc, base_atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, base_atk=base_atk, heal=heal,defType=defType)
    

    def effect(self,owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"



class Poison(dmgType.DamageType):
    def __init__(self, file,name, desc, base_atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, base_atk=base_atk, heal=heal,defType=defType)

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"



class Insanity(dmgType.DamageType):
    def __init__(self, file,name, desc, base_atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, base_atk=base_atk, heal=heal,defType=defType)
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"



class Control(dmgType.DamageType):
    def __init__(self, file,name, desc, base_atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, base_atk=base_atk, heal=heal,defType=defType)

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"