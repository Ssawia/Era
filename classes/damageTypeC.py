import sys

class DamageType:
    def __init__(self, name : str, desc : str, defType : str):
        self.name = name
        self.desc = desc
        self.defType = defType
    
    # No futuro implentar efeitos para certos tipos de dano
    def effect(self):
        pass



class Physical(DamageType):
    def __init__(self, name, desc, defType):
        super().__init__(name=name, desc=desc,defType=defType)
    

    def effect(self):
        return "Um ataque fisico"



class Magical(DamageType):
    def __init__(self, name, desc, defType):
        super().__init__(name=name, desc=desc,defType=defType)
    

    def effect(self):
        return "Um ataque magico"



def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


def getDamageTypeClass(data : list, damage_data : dict):
    dtypeList = []
    dtype : DamageType = None

    for c in data:
        dtype = str_to_class(damage_data[c]['class'])(name=damage_data[c]['name'],desc=damage_data[c]['desc'],defType=damage_data[c]['defType'])
        dtypeList.append(dtype)
    
    return dtypeList
