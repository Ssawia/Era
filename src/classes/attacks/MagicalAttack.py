import src.classes.entity_prototype as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.attacks.attackC as Attack
from helpers import isCrit,say_line,log,Log
from src.classes.ia_class_prototype import select_ai
from src.classes.temp.temp_class_handler import  Temp
from src.classes.effects.effect_class_prototype import AshenCurse


Attack = Attack.Attack
DamageType = dmgType.DamageType


class MagicalAttack(Attack):
    def __init__(self, attack_data, dmg_type):
        super().__init__(attack_data=attack_data, dmg_type=dmg_type)
    
    def doDamage(self, args: list = None):


        if args is not None:
            self.owner = args[0]
            self.queue = args[1]
            self.ai = args[2]


        obj: Chara.Character
        for obj in self.queue:
            for c in range(self.hits):
                obj.defend(self.name, self.dmgList, self.owner, obj)
        return True


class FireBallAttack(Attack):
    def __init__(self, attack_data, dmg_type):
        super().__init__(attack_data=attack_data, dmg_type=dmg_type)

    def doDamage(self, args: list = None):


        if args is not None:
            self.owner = args[0]
            self.queue = args[1]
            self.ai = args[2]


        obj: Chara.Character
        for obj in self.queue:
            for c in range(self.hits):
                obj.defend(self.name, self.dmgList, self.owner, obj)
        return True


class ReturnToAshAttack(Attack):
    def __init__(self, attack_data, dmg_type):
        super().__init__(attack_data=attack_data, dmg_type=dmg_type)

    def doDamage(self, args: list = None):



        if args is not None:
            self.owner = args[0]
            self.queue = args[1]
            self.ai = args[2]


        obj: Chara.Character
        for obj in self.queue:
            for c in range(self.hits):
                obj.defend(self.name, self.dmgList, self.owner, obj)
                effect = AshenCurse("ashen_curse",'Ashen Curse','The victim is marked with a smoldering brand that sears their flesh, slowly turning it to ash. This curse causes continuous burn damage over time, weakening both body and spirit. As the curse progresses, the afflicted’s movements become sluggish as their limbs blacken and crumble, and their resistance to fire-based attacks diminishes. Only through potent cleansing magic or a rare elemental salve can the curse be lifted, though scars remain, serving as a reminder of the fiery torment endured.',2,True,True,1,999,obj,False,None,self.owner)
                log(Log.INFO, f"Ashen Curse proc on {obj.name}")
                obj.effects_handler.add_effects([effect])

        return True