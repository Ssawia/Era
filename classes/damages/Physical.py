import classes.entitiesC as Chara
import classes.damages.damageTypeC as dmgType
import classes.attacks.attackC as Attack

class Physical(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    
    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.status.atk
        self.atk += dmgA

    def effect(self):
        return "Um ataque fisico"