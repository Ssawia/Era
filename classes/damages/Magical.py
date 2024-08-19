import classes.entitiesC as Chara
import classes.damages.damageTypeC as dmgType
import classes.attacks.attackC as Attack

class Telesma(dmgType.DamageType):
    def __init__(self, file,name, desc, atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Telesma']
        owner_dmg = owner.attributes.status.atkM
        final_dmg = dmgA + owner_dmg
        self.set_formula(owner_dmg,dmgA,final_dmg)
        self.atk += final_dmg
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"

class Fire(dmgType.DamageType):
    def __init__(self, file,name, desc, atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Fire']
        owner_dmg = owner.attributes.status.atkM
        final_dmg = dmgA + owner_dmg
        self.set_formula(owner_dmg,dmgA,final_dmg)
        self.atk += final_dmg
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        
        target.effects.append("[Burning]")

class Water(dmgType.DamageType):
    def __init__(self, file,name, desc, atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Water']
        owner_dmg = owner.attributes.status.atkM
        final_dmg = dmgA + owner_dmg
        self.set_formula(owner_dmg,dmgA,final_dmg)
        self.atk += final_dmg
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"

class Earth(dmgType.DamageType):
    def __init__(self, file,name, desc, atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Earth']
        owner_dmg = owner.attributes.status.atkM
        final_dmg = dmgA + owner_dmg
        self.set_formula(owner_dmg,dmgA,final_dmg)
        self.atk += final_dmg
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"

class Wind(dmgType.DamageType):
    def __init__(self, file,name, desc, atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Wind']
        owner_dmg = owner.attributes.status.atkM
        final_dmg = dmgA + owner_dmg
        self.set_formula(owner_dmg,dmgA,final_dmg)
        self.atk += final_dmg
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"

class Arcane(dmgType.DamageType):
    def __init__(self, file,name, desc, atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Arcane']
        owner_dmg = owner.attributes.status.atkM
        final_dmg = dmgA + owner_dmg
        self.set_formula(owner_dmg,dmgA,final_dmg)
        self.atk += final_dmg
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"

class Blood(dmgType.DamageType):
    def __init__(self, file,name, desc, atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Blood']
        owner_dmg = owner.attributes.status.atkM
        final_dmg = dmgA + owner_dmg
        self.set_formula(owner_dmg,dmgA,final_dmg)
        self.atk += final_dmg
    

    def effect(self,owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"

class Poison(dmgType.DamageType):
    def __init__(self, file,name, desc, atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Poison']
        owner_dmg = owner.attributes.status.atkM
        final_dmg = dmgA + owner_dmg
        self.set_formula(owner_dmg,dmgA,final_dmg)
        self.atk += final_dmg
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"

class Insanity(dmgType.DamageType):
    def __init__(self, file,name, desc, atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Insanity']
        owner_dmg = owner.attributes.status.atkM
        final_dmg = dmgA + owner_dmg
        self.set_formula(owner_dmg,dmgA,final_dmg)
        self.atk += final_dmg
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"

class Control(dmgType.DamageType):
    def __init__(self, file,name, desc, atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Control']
        owner_dmg = owner.attributes.status.atkM
        final_dmg = dmgA + owner_dmg
        self.set_formula(owner_dmg,dmgA,final_dmg)
        self.atk += final_dmg
    

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque magico"