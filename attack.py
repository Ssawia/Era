from character import Character

class DamageType:
    def __init__(self, name : str, desc : str, defType : str):
        self.name = name
        self.desc = desc
        self.defType = defType
    

    def effect(self):
        pass
     



class Attack:
    def __init__(self, chara : Character, damage : float, hits : int, _type : DamageType):
        self.name = "attack"
        self.desc = "A physical attack"
        self.owner = chara
        self.damage = damage
        self.hits = hits
        self.type = _type
    



    def doDamage(self, obj: Character):

        atk_base = self.owner._atk

        for c in range(self.hits):
            damage = self.damage + atk_base
            obj.defend(damage, self.type)
