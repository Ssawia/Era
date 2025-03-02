from __future__ import annotations

import src.classes.entity_prototype as character
import uuid
from helpers import log,Log



class Temp:
    """
    Classe responsável por definir a estrutura base de um atributo temporário dentro em um objeto.
    """


    def __init__(self, status: str, typo: str, turn: int,time: int,value:int,active:bool,is_turn:bool,is_time:bool, active_flag: str | None) -> None:
        self.uid = uuid.uuid4()

        self.status = status
        self.typo = typo
        self.turn = turn
        self.time = time
        self.value = value
        self.active = active
        self.isTurn = is_turn
        self.isTime = is_time
        self.active_flag = active_flag




class TempHandler:
    """
    Classe responsável por gerenciar os temp em um objeto
    """

    def __init__(self,parent, name) -> None:
        self.uid = uuid.uuid4()
        self._parent = parent
        self.name = name
        self.list_temps: list[Temp] = []
        self.temps_info: dict = {}
        self.flags = []


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


    def remove_temp(self, all_temp: bool = False, list_temp: list[Temp] | None = None, flags: list[str]  = None) -> None:
        """
        Remove a temp with the Objet, UID or the Flag
        """
        parent: character.Character = self._parent.return_parent()


        if flags is not None and len(flags) > 0:
            if list_temp is None:
                list_temp = []
            for flag in flags:
                for temp in self.list_temps:
                    if flag == temp.active_flag:
                        log(Log.DEBUG, f"[{flag}] Temp Status: {temp.status} flagged", f"[{parent.name}][Attributes][TempHandler][Flag]")
                        list_temp.append(temp)

        if all_temp:
            self.list_temps = []
            print(f"[LOG][TempHandler] All temps removed")
            log(Log.DEBUG, "All temps removed", f"[{parent.name}][Attributes][TempHandler]")

        if list_temp is not None:
            for temp in list_temp:
                if temp in self.list_temps:
                    self.list_temps.remove(temp)

                    if isinstance(self._parent.return_parent(), character.Character):
                        log(Log.DEBUG, f"Temp Status: {temp.status} removed", f"[{parent.name}][Attributes][TempHandler]")

                else:
                    log(Log.WARNING,"Temp not in list to remove",  f"[{parent.name}][Attributes][TempHandler]")

        else:
            print("[ERROR][TempHandler] Temp não existe")


    def update_time_turn(self, turn: int = 1 ,time: float = 1.0) -> None:
        parent: character.Character = self._parent.return_parent()
        log_append = f"[{parent.name}][Attributes][TempHandler]"
        log(Log.DEBUG,f"Updating Temps: {len(self.list_temps)}", log_append)

        temps_to_remove = []
        flags = []

        for tmp in self.list_temps:
            log(Log.DEBUG,f"Temp: {tmp.uid}", log_append)
            if tmp.isTurn and tmp.active_flag is None:
                if tmp.turn > 0:
                    tmp.turn -= turn

                if tmp.turn <= 0:
                    log(Log.DEBUG,f"Temp {tmp.status} has 0 turn", log_append)
                    temps_to_remove.append(tmp)

            if tmp.active_flag is None:
                if tmp.isTime and (tmp.time - time) > 0:
                    tmp.turn -= time
                elif tmp.time < 0:
                    self.remove_temp(list_temp=[tmp])

            if tmp.active_flag is not None:
                log(Log.DEBUG, f"Temp {tmp.status} has a flag {tmp.active_flag}", log_append)
                flags.append(tmp.active_flag)


        self.flags = flags

        self.remove_temp(list_temp=temps_to_remove)
        self.update_temp()



    def update_temp(self) -> None:
        """
        Atualiza a lista de atributos do temps_info com todos os bonus dos Temps
        """
        tmp = {}

        parent: character.Character = self._parent.return_parent()
        log_append = f"[{parent.name}][Attributes][TempHandler]"
        log(Log.DEBUG, f"Updating Temps Dict: {len(self.list_temps)}", log_append)


        for temp in self.list_temps:
            if temp.status not in tmp.keys():
                tmp[temp.status] = []
                log(Log.DEBUG, f"Updating Temp info: {temp.uid}", log_append)
                data =  {temp.typo: temp.value, "turns": temp.turn, "time": temp.time}
                tmp[temp.status].append(data)
            else:
                log(Log.DEBUG, f"Updating Temp info: {temp.uid}", log_append)
                data =  {temp.typo: temp.value, "turns": temp.turn, "time": temp.time}
                tmp[temp.status].append(data)

        self.temps_info = tmp


    def get_add_bonus(self,status: str,typo: str) -> float:
        """
        Retorna todos os bonus adicionais dos Temps somados
        """
        value: float = 0.0
        if status in self.temps_info.keys():
            print(self.temps_info[status])
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