
class Component:
    _name: str
    active: bool


class Attributes(Component):
    def __init__(self,name: str,active: bool) -> None:
        super().__init__()
        self._name = name
        self.name = name
        self.hp = 10
        self.active = active



class Status(Component):
    def __init__(self,name: str,active: bool) -> None:
        super().__init__()
        self.name = name
        self.active = active


class Entity:
    sprite : str = ''
    x : float = 0
    y : float = 0
    components: list[Component] = []


    def add_comp(self,comp_c : Component):
        if comp_c is not None and comp_c not in self.components:
            self.components.append(comp_c)
    

    def check_if_comp_exist(self, comp_c, rcomp: bool = False) -> Component | None:
        for attr in self.components:
            if isinstance(attr, comp_c):
                return attr if rcomp else None
        return None
    
    def return_comp(self,comp_c):
        return self.check_if_comp_exist(comp_c,rcomp=True)
        




class Character(Entity):
    def __init__(self, name,sprite,x,y):
        super().__init__()
        self.name = name
        self.sprite = sprite
        self.x = x
        self.y = y

pre-asd = "a"

print(_)

attr = Attributes("Attributes", True)


flandre = Character("flandre","flandre.png",10,7)



flandre.add_comp(attr)

comp: Attributes | None = flandre.return_comp(Attributes)
if comp is not None:
    print(comp)








        

