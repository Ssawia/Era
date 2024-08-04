from __future__ import annotations

import classes.entitiesC
import classes.damageTypeC as dmgType
import sys


#Classe usada para definir o tipo de dano dos ataques, como ataque fisico ou ataque magico




class Attack:
    def __init__(self, name : str, desc : str,  damage : float, hits : int, dmgType : list, chara : classes.entitiesC.Character = None):
        self.name = name
        self.desc = desc
        self.owner = chara
        self.damage = damage
        self.hits = hits
        self.types = dmgType
    



    def doDamage(self, obj: classes.entitiesC.Character):

        atk_base = self.owner._atk

        for c in range(self.hits):
            damage = self.damage + atk_base
            obj.defend(damage, self.types)
    
    def imwho(self):
       return self.name
    



class AttackFds(Attack):
  def __init__(self, name, desc, damage,hits, dmgType):
    super().__init__(name=name, desc=desc,damage=damage,hits=hits, dmgType=dmgType)





def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)