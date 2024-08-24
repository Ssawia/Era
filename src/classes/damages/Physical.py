import src.classes.entitiesC as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.attacks.attackC as Attack

class Slash(dmgType.DamageType):
    def __init__(self, file,name, desc, atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    
    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Slash']
        owner_dmg = owner.attributes.status.atk
        final_dmg = dmgA + owner_dmg
        self.set_formula(owner_dmg,dmgA,final_dmg)
        self.atk += final_dmg

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque fisico"

class Strike(dmgType.DamageType):
    def __init__(self, file,name, desc, atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    
    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Strike']
        owner_dmg = owner.attributes.status.atk
        final_dmg = dmgA + owner_dmg
        self.set_formula(owner_dmg,dmgA,final_dmg)
        self.atk += final_dmg

    def effect(self, owner : Chara.Character, target : Chara.Character ):
        return "Um ataque fisico"

class Thrust(dmgType.DamageType):
    def __init__(self, file,name, desc, atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    
    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.elements['Thrust']
        owner_dmg = owner.attributes.status.atk
        final_dmg = dmgA + owner_dmg
        self.set_formula(owner_dmg,dmgA,final_dmg)
        self.atk += final_dmg

    def effect(self, owner : Chara.Character, target : Chara.Character):
        return "Um ataque fisico"