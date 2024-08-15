import classes.entitiesC as Chara
import classes.damages.damageTypeC as dmgType
import classes.attacks.attackC as Attack

class Slash(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    
    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Slash']
        self.formula = f"[BASE]{self.atk}+{dmgA}[{self.name}]={self.atk + dmgA}"

        self.atk += dmgA

    def effect(self):
        return "Um ataque fisico"

class Strike(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    
    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Strike']
        self.formula = f"[BASE]{self.atk}+{dmgA}[{self.name}]={self.atk + dmgA}"
        self.atk += dmgA

    def effect(self):
        return "Um ataque fisico"

class Thrust(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    
    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Thrust']
        self.formula = f"[BASE]{self.atk}+{dmgA}[{self.name}]={self.atk + dmgA}"
        self.atk += dmgA

    def effect(self):
        return "Um ataque fisico"