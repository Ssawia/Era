import classes.entitiesC as Chara
import classes.damages.damageTypeC as dmgType
import classes.attacks.attackC as Attack

class Healing(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        addToHeal = owner.attributes.atkm
        print(f"[{self.name}]{self.heal}+{addToHeal}={self.heal+addToHeal}")
        self.heal += addToHeal
    

    def effect(self):
        return "Um ataque magico"