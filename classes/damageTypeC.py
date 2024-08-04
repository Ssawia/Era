

class DamageType:
    def __init__(self, name : str, desc : str, defType : str):
        self.name = name
        self.desc = desc
        self.defType = defType
    
    # No futuro implentar efeitos para certos tipos de dano
    def effect(self):
        pass
