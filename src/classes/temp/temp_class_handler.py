from __future__ import annotations
from dataclasses import dataclass
import src.classes.entity_prototype as character
import uuid
from helpers import log,Log


@dataclass
class Temp:
    """
    Classe responsável por definir a estrutura base de um atributo temporário dentro em um objeto.
    """

    status: str
    typo: str
    turn: int
    time: int
    value: int
    active: bool
    isTurn: bool
    isTime: bool
    active_uid: uuid



class TempHandler:
    """
    Classe responsável por gerenciar os temp em um objeto
    """
    list_temps: list[Temp] = []
    temps_info: dict = {}

    def __init__(self,parent) -> None:
        self._parent = parent


    def add_temp(self, temp: list[Temp]) -> None:
        """
        Adiciona temps na lista, além de atualizar o dicionário de atributos com update_temp_turn()
        Também atualiza os atributos caso o _parent ser uma instância do objeto Attributes.
        """
        for tmp in temp:
            self.list_temps.append(tmp)
            if isinstance(self._parent.return_parent(), character.Character):
                parent: character.Character = self._parent.return_parent()

                log(Log.DEBUG, f"Temp Status: {tmp.status} added.", f"[{parent.name}][Attributes][TempHandler]")



        self.update_temp()
        if isinstance(self._parent,character.Attributes):
            parent: character.Character = self._parent.return_parent()

            log(Log.DEBUG, f"Parent is a instance of Attributes, updating the the attributes", f"[{parent.name}][Attributes][TempHandler]")
            self._parent.update_attributes()
        else:
            log(Log.ERROR, f"Is not a Instance: {type(self._parent)}", f"[Attributes][TempHandler]")


    def remove_temp(self, all_temp: bool = False, list_temp: list[Temp] | None = None) -> None:
        """
        Remove a temp with the objet or by the UID
        """
        if all_temp:
            self.list_temps = []
            print(f"[LOG][TempHandler] All temps removed")

        if list_temp is not None:
            for temp in list_temp:
                self.list_temps.remove(temp)

                if isinstance(self._parent.return_parent(), character.Character):
                    parent: character.Character = self._parent.return_parent()
                    log(Log.DEBUG, f"Temp Status: {temp.status} removed", f"[{parent.name}][Attributes][TempHandler]")

                if isinstance(self._parent, character.Attributes):
                    parent: character.Character = self._parent.return_parent()
                    log(Log.DEBUG, f"Parent is a instance of Attributes, updating the the attributes", f"[{parent.name}][Attributes][TempHandler]")
                    self._parent.update_attributes()

        else:
            print("[ERROR][TempHandler] Temp não existe")


    def update_time_turn(self, turn: int = 1 ,time: float = 1.0) -> None:

        for tmp in self.list_temps:
            if tmp.isTurn and tmp.turn > 0:
                tmp.turn -= turn
            elif tmp.turn < 0:
                self.remove_temp(list_temp=[tmp])

            if tmp.isTime and (tmp.time - time) > 0:
                tmp.turn -= time
            elif tmp.time < 0:
                self.remove_temp(list_temp=[tmp])

        self.update_temp()



    def update_temp(self) -> None:
        """
        Atualiza a lista de atributos do temps_info com todos os bonus dos Temps
        """
        tmp = {}
        for temp in self.list_temps:
            if temp.status not in tmp.keys():
                tmp[temp.status] = []
                data =  {temp.typo: temp.value, "turns": temp.turn, "time": temp.time}
                tmp[temp.status].append(data)
            else:
                data =  {temp.typo: temp.value, "turns": temp.turn, "time": temp.time}
                tmp[temp.status].append(data)

        self.temps_info = tmp


    def get_add_bonus(self,status: str,typo: str) -> float:
        """
        Retorna todos os bonus adicionais dos Temps somados
        """
        value: float = 0.0
        if status in self.temps_info.keys():
            for bonus in self.temps_info[status]:
                if typo in list(bonus.keys()):
                    if typo == "add":
                        value += bonus[typo]

        return value



    def get_mult_bonus(self,status: str,typo: str) -> float:
        """
        Retorna todos os bonus multiplicadores dos Temps somados
        """

        value: float = 1
        if status in self.temps_info.keys():
            for bonus in self.temps_info[status]:
                if typo in list(bonus.keys()):
                    if typo == "mult":
                        value += bonus[typo]

        return value