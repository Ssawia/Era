



class Character:
    def __init__(self, data : dict, type : str):
        self._id = data['_id']
        self._name = data['name']
        self.nick = data['nick']
        self._hp = data['hp']
        self._maxhp = self._hp
        self._atk = data['atk']
        self._def = data['def']

        self.type = type


    def defend(self, damage):
        pass

    def attack(self, obj):
        pass








