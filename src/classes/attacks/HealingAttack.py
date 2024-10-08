import src.classes.entity_prototype as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.attacks.attackC as Attack
from src.classes.ia_class_prototype import select_ai


Attack = Attack.Attack

class HealingAttack(Attack):
    def __init__(self, attack_data, dmg_type):
        super().__init__(attack_data=attack_data, dmg_type=dmg_type)
    

    def doDamage(self, owner : Chara.Character, queue: list, ai = False,  args: list = None):

        if args is not None:
            owner = args[0]
            queue = args[1]
            ai = args[2]


        if not ai:
            self.init_select(queue)
            queue = self.check_target(owner)

        obj : Chara.Character 

        for obj in queue:
            for c in range(self.hits):
                obj.healing(self.dmgList)

        return True  