import classes.entitiesC as Chara
import classes.damages.damageTypeC as dmgType
import classes.attacks.attackC as Attack

class Telesma(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Telesma']
        self.formula = f"[BASE]{self.atk}+{dmgA}[{self.name}]={self.atk + dmgA}"
        self.atk += dmgA
    

    def effect(self):
        return "Um ataque magico"

class Fire(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Fire']
        self.formula = f"[BASE]{self.atk}+{dmgA}[{self.name}]={self.atk + dmgA}"
        self.atk += dmgA
    

    def effect(self):
        return "Um ataque magico"

class Water(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Water']
        self.formula = f"[BASE]{self.atk}+{dmgA}[{self.name}]={self.atk + dmgA}"
        self.atk += dmgA
    

    def effect(self):
        return "Um ataque magico"

class Earth(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Earth']
        self.formula = f"[BASE]{self.atk}+{dmgA}[{self.name}]={self.atk + dmgA}"
        self.atk += dmgA
    

    def effect(self):
        return "Um ataque magico"

class Wind(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Wind']
        self.formula = f"[BASE]{self.atk}+{dmgA}[{self.name}]={self.atk + dmgA}"
        self.atk += dmgA
    

    def effect(self):
        return "Um ataque magico"

class Arcane(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Arcane']
        self.formula = f"[BASE]{self.atk}+{dmgA}[{self.name}]={self.atk + dmgA}"
        self.atk += dmgA
    

    def effect(self):
        return "Um ataque magico"

class Blood(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Blood']
        self.formula = f"[BASE]{self.atk}+{dmgA}[{self.name}]={self.atk + dmgA}"
        self.atk += dmgA
    

    def effect(self):
        return "Um ataque magico"

class Poison(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Poison']
        self.formula = f"[BASE]{self.atk}+{dmgA}[{self.name}]={self.atk + dmgA}"
        self.atk += dmgA
    

    def effect(self):
        return "Um ataque magico"

class Insanity(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Insanity']
        self.formula = f"[BASE]{self.atk}+{dmgA}[{self.name}]={self.atk + dmgA}"
        self.atk += dmgA
    

    def effect(self):
        return "Um ataque magico"

class Control(dmgType.DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Control']
        self.formula = f"[BASE]{self.atk}+{dmgA}[{self.name}]={self.atk + dmgA}"
        self.atk += dmgA
    

    def effect(self):
        return "Um ataque magico"