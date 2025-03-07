from tkinter.ttk import Treeview

import src.classes.entity_prototype as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.attacks.attackC as Attack
from helpers import isCrit
from src.classes.ia_class_prototype import select_ai

Attack = Attack.Attack


class PhysicalAttack(Attack):
    def __init__(self, attack_data, dmg_type):
        super().__init__(attack_data=attack_data, dmg_type=dmg_type)
