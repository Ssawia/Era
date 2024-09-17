import src.classes.entitiesC as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.attacks.attackC as Attack

Attack = Attack.Attack

class HealingAttack(Attack):
    def __init__(self, attack_data, dmg_type):
        super().__init__(attack_data=attack_data, dmg_type=dmg_type)
    

    def doDamage(self, owner : Chara.Character, queue: list, ai = False):
        if not ai:
            self.init_select(queue)
            queue = self.check_target(owner)

        obj : Chara.Character 

        for obj in queue:
            for c in range(self.hits):
                obj.healing(self.dmgList)

        return True  