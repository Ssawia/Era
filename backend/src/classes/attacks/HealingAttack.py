import src.classes.entity.character as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.attacks.attackC as Attack
from src.classes.ia_class_prototype import select_ai


Attack = Attack.Attack

class HealingAttack(Attack):
    def __init__(self, attack_data, dmg_type):
        super().__init__(attack_data=attack_data, dmg_type=dmg_type)
    

    