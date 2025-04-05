import src.classes.entity.character as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.attacks.attackC as Attack
from helpers import isCrit,say_line,log,Log
from src.classes.ia_class_prototype import select_ai
from src.classes.temps.temp_class_handler import  Temp
from src.classes.effects.ashen_curse import AshenCurse


Attack = Attack.Attack
DamageType = dmgType.DamageType


class MagicalAttack(Attack):
    def __init__(self, attack_data, dmg_type):
        super().__init__(attack_data=attack_data, dmg_type=dmg_type)
    

class FireBallAttack(Attack):
    def __init__(self, attack_data, dmg_type):
        super().__init__(attack_data=attack_data, dmg_type=dmg_type)


class ReturnToAshAttack(Attack):
    def __init__(self, attack_data, dmg_type):
        super().__init__(attack_data=attack_data, dmg_type=dmg_type)

