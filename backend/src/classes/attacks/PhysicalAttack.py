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