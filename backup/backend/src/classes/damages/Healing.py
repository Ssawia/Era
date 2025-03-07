import src.classes.entity_prototype as Chara
import src.classes.damages.damageTypeC as dmgType

class Healing(dmgType.DamageType):
    def __init__(self, file,name, desc, min_atk,max_atk,min_heal,max_heal ,defType, effects):
        super().__init__(file=file,name=name, desc=desc, min_atk=min_atk, max_atk=max_atk,min_heal=min_heal,max_heal=max_heal ,defType=defType, effects=effects)
    

    def set_attack(self, owner: Chara.Character):
        add_to_heal = 0

        if check_if_attributes_exist(owner):
            add_to_heal = owner.attributes.status.atkM
        self.heal += add_to_heal
    