import src.classes.entity_prototype as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.attacks.attackC as Attack
from helpers import isCrit,say_line
from src.classes.ia_class_prototype import select_ai
from src.classes.temp.temp_class_handler import  Temp


Attack = Attack.Attack
DamageType = dmgType.DamageType


class MagicalAttack(Attack):
    def __init__(self, attack_data, dmg_type):
        super().__init__(attack_data=attack_data, dmg_type=dmg_type)
    
    def doDamage(self, owner : Chara.Character, queue: list, ai = False, args: list = None):

        if args is not None:
            owner = args[0]
            queue = args[1]
            ai = args[2]



        if not ai:
            self.init_select(queue)
            queue = self.check_target(owner)

        crit = isCrit(owner.attributes.status.crit)


        obj : Chara.Character
        for obj in queue:
            for c in range(self.hits):
                obj.defend(self.name,self.dmgList, owner, obj, crit)
            
        return True


class FireBallAttack(Attack):
    def __init__(self, attack_data, dmg_type):
        super().__init__(attack_data=attack_data, dmg_type=dmg_type)

    def doDamage(self, owner: Chara.Character, queue: list, ai=False, args: list = None):



        if args is not None:
            owner = args[0]
            queue = args[1]
            ai = args[2]

        if not ai:
            self.init_select(queue)
            queue = self.check_target(owner)

        crit = isCrit(owner.attributes.status.crit)
        temp1 = Temp("Fire", "mult", 2, 0, 1, True, True, False, None)
        temp2 = Temp("Fire", "add", 2, 0, 10, True, True, False, None)

        owner.attributes.temp_handler.add_temp([temp2,temp1])

        obj: Chara.Character
        for obj in queue:
            for c in range(self.hits):
                obj.defend(self.name, self.dmgList, owner, obj, crit)

        return True