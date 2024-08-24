import src.classes.entitiesC as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.attacks.attackC as Attack

class Healing(dmgType.DamageType):
    def __init__(self, file,name, desc, atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        addToHeal = owner.attributes.status.atkM
        self.heal += addToHeal
    

    def effect(self):
        return "Um ataque magico"