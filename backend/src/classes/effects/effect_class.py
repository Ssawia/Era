from __future__ import annotations
import uuid
import abstraction
import src.classes.entity_prototype as ch
import helpers
from math import trunc
#import src.classes.temps.temp_class_handler as tp

class Effect:
    """_summary_ Classe responsável por definir os efeitos de vários tipos, como efeito de status, efeito de batalha, efeito de habilidade
    """
    def __init__(self, typo: str, name: str, desc: str, turns: int, active: bool, is_stackable: bool,stacks: int, max_stacks: int, giver: ch.Character, character: ch.Character, has_temp: bool, temp_objs: list[dict], obj_values: dict, event: str):
        """
        Parameters
        ----------
        typo : str | O tipo de efeito
        name : str | O nome do efeito
        desc : str | A descrição do efeito
        turns : int | Os turnos do efeito
        active : bool | Se o efeito está ativo ou não
        is_stackable: bool | Se o efeito é estácavel
        stacks : int | Quantos stacks o efeito tem
        max_stacks: int | O número máximo de stacks
        giver : Character, optional | O objeto que criou o efeito
        character : Character, optional | O objeto que o efeito está dentro
        has_temp : bool | Se o efeito tem temps
        temps_data : list[dict], optional | As informações de temps
        obj_values: dict, optional | Parámetros especias do efeito
        event: str | o tipo de evento que vai acionar esse efeito
        """
        
        self.uuid: uuid.UUID = uuid.uuid4()
        self.typo: str = typo
        self.name: str = name
        self.desc: str = desc
        self.main_turn: int = turns
        self.turn: int = self.main_turn
        self.active: bool = active
        self.is_stackable: bool = is_stackable
        self.main_stacks: int = stacks
        self.stacks:int = self.main_stacks

        self.max_stacks: int = max_stacks
        self.has_temp: bool = has_temp

        self.temp_objs: list[dict] =  temp_objs
        self.objs_temp_data: list[dict] = []
        self.obj_values: dict = obj_values
        self.event: str = event


        self.owner : ch.Character| None = character
        self.giver: ch.Character | None = giver
        self.start()
    

    def start(self) -> None:
        #print(self.obj_values)
        pass
        
    

    def init_effect(self) -> None:
        if self.active and self.name not in self.owner.attributes.temp_handler.flags:
            for temp_obj in self.temp_objs:
                if temp_obj["event"] == "init":
                    temp_id = temp_obj['id']
                    temp_target = temp_obj['target']
                    temp_flag = temp_obj["flag"]
                    
                    owner: ch.Character

                    if temp_target == "self":
                        owner = self.giver
                    elif temp_target == "target":
                        owner = self.owner
                    
                    temp = abstraction.get_temp_from_id(temp_id,temp_flag)
                    owner.attributes.temp_handler.add_temp([temp])

                    temp_data = {"obj": self.giver, "temp": temp, "flag": temp_flag}
                    self.objs_temp_data.append(temp_data)

                    owner.attributes.update_attributes()
                    owner.attributes.update_attributes_bonus()
                    owner.attributes.update_elements()
                    owner.attributes.update_resistances()


    def process_effect(self) -> bool | None:
        pass

    def end_effect(self) -> None:
        self.active = False
        helpers.log(helpers.Log.INFO,f"Effect {self.name} has ended", f"[{self.owner.name}][EffectHandler][Effect]")

        if self.has_temp:
            for data in self.objs_temp_data:
                obj: ch.Character
                flag = data['flag']
                obj = data['obj']
                
                if flag == self.name:
                    helpers.log(helpers.Log.INFO, f"{obj.name} tem a flag {self.name} temp, removendo", f"[{obj.name}][EffectHandler][Effect]")
                    obj.attributes.temp_handler.remove_temp(flags=[self.name])
                



