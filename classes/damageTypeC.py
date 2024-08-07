from __future__ import annotations
import sys
import classes.entitiesC as Chara

class DamageType:
    def __init__(self, name : str, desc : str, defType : str, atk : float = None, heal : float = None):
        self.name = name
        self.desc = desc
        self.defType = defType
        self.atk = atk
        self.heal = heal
    
    # No futuro implentar efeitos para certos tipos de dano
    def effect(self):
        pass


    def setAttack(self,owner : Chara.Character):
        pass

    def setHeal(self, owner : Chara.Character):
        pass
        



class Physical(DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    
    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.atk

        print(f"[{self.name}]{self.atk}+{dmgA}={self.atk+dmgA}")

        self.atk += dmgA

    def effect(self):
        return "Um ataque fisico"



class Magical(DamageType):
    def __init__(self, name, desc, atk, heal,defType):
        super().__init__(name=name, desc=desc, atk=atk, heal=heal,defType=defType)
    

    def setAttack(self, owner: Chara.Character):
        dmgA = owner.attributes.atkm
        print(f"[{self.name}]{self.atk}+{dmgA}={self.atk+dmgA}")
        self.atk += dmgA
    

    def effect(self):
        return "Um ataque magico"



def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


def getDamageTypeClass(data : list, damage_data : dict, damages : list):
    dtypeList = []
    dtype : DamageType = None
    i = 0

    atk = 0
    heal = 0
    for c in data:
        if 'atk' in damages[i].keys():
            atk = damages[i]['atk']
        if 'heal' in damages[i].keys():
            heal = damages[i]['heal']

        dtype = str_to_class(damage_data[c]['class'])(name=damage_data[c]['name'],desc=damage_data[c]['desc'],atk=atk,heal=heal,defType=damage_data[c]['defType'])
        dtypeList.append(dtype)
        i += 1
    
    return dtypeList
