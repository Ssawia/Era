import src.classes.entity_prototype as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.effects.effect_class_prototype as effect
import src.classes.temp.temp_class_handler as Temp
from helpers import Log, log

import random

class Telesma(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType)
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"



class Fire(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType)


    def effect(self, owner : Chara.Character, target : Chara.Character):
        chance_to_burn = 100

        num = random.randint(1,100)
        if num <= chance_to_burn:
            temp_main = Temp.Temp("faith", "add", 1, 0, 10, True,True,False,target.uuid)
            owner.attributes.temp_handler.add_temp([temp_main])
            effect_main = effect.AshenCurse("ashen_curse",'Ashen Curse','The victim is marked with a smoldering brand that sears their flesh, slowly turning it to ash. This curse causes continuous burn damage over time, weakening both body and spirit. As the curse progresses, the afflicted’s movements become sluggish as their limbs blacken and crumble, and their resistance to fire-based attacks diminishes. Only through potent cleansing magic or a rare elemental salve can the curse be lifted, though scars remain, serving as a reminder of the fiery torment endured.',2,True,True,1,999,target,False,None,owner)
            log(Log.INFO, f"Ashen Curse proc on {target.name}")
            target.effects_handler.add_effects([effect_main])
            



class Water(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType)
    

    def effect(self, owner : Chara.Character, target : Chara.Character):

        return "Um ataque magico"





class Earth(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType)
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"




class Wind(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType)
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"





class Arcane(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType)
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"




class Blood(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType)
    

    def effect(self,owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"



class Poison(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType)

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"



class Insanity(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType)
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"



class Control(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType)

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"