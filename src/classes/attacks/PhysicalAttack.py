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
    
    def doDamage(self, owner : Chara.Character | None = None, queue: list | None = None, ai = False,  args: list = None):


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