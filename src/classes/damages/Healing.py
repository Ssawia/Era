import src.classes.entitiesC as Chara
import src.classes.damages.damageTypeC as dmgType

class Healing(dmgType.DamageType):
    def __init__(self, file,name, desc, base_atk, heal,defType):
        super().__init__(file=file,name=name, desc=desc, base_atk=base_atk, heal=heal,defType=defType)
    

    def set_attack(self, owner: Chara.Character):
        add_to_heal = 0

        if check_if_attributes_exist(owner):
            add_to_heal = owner.attributes.status.atkM
        self.heal += add_to_heal
    

    def effect(self):
        return "Um ataque magico"