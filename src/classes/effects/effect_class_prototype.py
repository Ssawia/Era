from __future__ import annotations
import src.classes.entity_prototype as Character
import uuid


class Effect:
    def __init__(self, typo, name, desc, turns, active, is_stackable,stacks, character):
        self.uuid = uuid.uuid4()
        self.typo = typo
        self.name = name
        self.desc = desc
        self.turn = turns
        self.active = active
        self.is_stackable = is_stackable
        self.stacks = stacks
        self.owner : Character = character



    def process_effect(self):
        pass

    def del_effect(self):
        pass




class Burn(Effect):
    def __init__(self,typo,name,desc,turns,active,is_stackable,stacks,character):
        super().__init__(typo=typo,name=name,desc=desc,turns=turns,active=active,is_stackable=is_stackable,stacks=stacks,character=character)


    def process_effect(self):
        if self.turn > 0 and self.active:
            dmg = self.owner.attributes.status.hp * (0.1 * self.stacks)
            print(f"{self.owner.name} tomou {dmg} de burn")
            self.owner.attributes.status.hp -= dmg
            self.turn -= 1
            return True
        elif self.turn <= 0:
            print("Efeito burn Acabou")
            self.active = False
            return False