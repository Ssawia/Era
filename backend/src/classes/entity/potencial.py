class Potencial:

    def __init__(self, potential) -> None:
        self.vitality: float = potential["vitality"]
        self.constitution: float = potential["constitution"]
        self.strength: float  = potential["strength"]
        self.fortitude: float = potential["fortitude"]
        self.attunement: float = potential["attunement"]
        self.intelligence: float = potential["intelligence"]
        self.will: float = potential["will"]
        self.faith: float = potential["faith"]
        self.arcane: float = potential["arcane"]
        self.dexterity: float = potential["dexterity"]
        self.fortune: float = potential["fortune"]

        self.bonus = []