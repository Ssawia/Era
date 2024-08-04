from __future__ import annotations
#Provavelmente isso não é a melhor maneira de implementar varias classes, mas por enquanto vai dar certo, confia

#Classe usada para definir o tipo de dano dos ataques, como ataque fisico ou ataque magico
class DamageType:
    def __init__(self, name : str, desc : str, defType : str):
        self.name = name
        self.desc = desc
        self.defType = defType
    
    # No futuro implentar efeitos para certos tipos de dano
    def effect(self):
        pass


class Attack:
    def __init__(self, name : str, desc : str,  damage : float, hits : int, dmgType : DamageType, chara : Character = None):
        self.name = name
        self.desc = desc
        self.owner = chara
        self.damage = damage
        self.hits = hits
        self.type = dmgType
    



    def doDamage(self, obj: Character):

        atk_base = self.owner._atk

        for c in range(self.hits):
            damage = self.damage + atk_base
            obj.defend(damage, self.type)
    

    def getrekt(self):
        print("Danm boy")


class AttackFds(Attack):
  def __init__(self, name, desc, damage,hits, dmgType):
    super().__init__(name=name, desc=desc,damage=damage,hits=hits, dmgType=dmgType)

  def getrekt(self):
      return "Gyatt Girl, skibidi"



    






class Character:
    def __init__(self, data : dict, _type : str):
        self._id = data['_id']
        self._name = data['name']
        self.nick = data['nick']
        self.type = _type
        self.alive = True


        self._hp = data['hp']
        self._maxhp = self._hp
        self._atk = data['atk']
        self._atkM = data['atkM']
        self._def = data['def']
        self._defM = data['defM']
        self._spd = data['spd']

        

    def isAlive(self):
        if self._hp <= 0:
            self.alive = False


    def defend(self, damage : float, damageType : DamageType):

        self.isAlive()

        if self.alive:
            if damageType.defType == "PhysicalDamage":
                damage_final = damage - self._def
            elif damageType.defType == "MagicalDamage":
                damage_final = damage - self._defM
            
            self.hp -= damage_final

    def attack(self, obj : Character, attack : Attack):
        attack.doDamage(obj)










