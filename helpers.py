from __future__ import annotations

from math import trunc
from tkinter.ttk import Treeview

import src.classes.entity_prototype as entities
import src.classes.temp.temp_class_handler as tp
import random
from typing import List
from enum import Enum
import json

config = json.load(open('config/config.json'))
is_debug = config['debug']

class Log(Enum):
    DEBUG = '\033[32m'
    CHAT = '\033[94m'
    INFO = '\033[34m'
    ERROR = '\033[31m'
    WARNING = '\033[33m'
    MAIN = '\033[35m'
    EVENT = '\033[36m'

def log(typ: Log, message: str, append : str = ''):
    reset = '\033[0m'


    if is_debug and typ == Log.DEBUG:
        msg = f"[{typ.value}{typ.name}{reset}]{append} {message}"
        print(msg)
    else:
        msg = ''
        print(msg,end="")

    if typ != Log.DEBUG:
        msg = f"[{typ.value}{typ.name}{reset}]{append} {message}"
        print(msg)






def get_potencial_string(number: float) -> str:
    potencial = {
        1.0: "G",
        1.1: "F",
        1.2: "E",
        1.3: "D",
        1.4: "C",
        1.5: "B",
        1.6: "A",
        1.7: "S",
        1.8: "SS",
        1.9: "SSS",
        2.0: "EX"
    }

    if 1.0 <= number <= 2.0:
        return potencial[number]
    else:
        return potencial[1.0]


def show_info_chara(obj : entities.Character):
    if obj.alive:
        alive = "Alive"
    else:
        alive = "Dead"

    data = f'''
[{obj.name}]-->[Uuid: {obj.uuid}]-->[{alive}]
[Attributes]-->[Uuid: {obj.attributes.uid}]
[TempHandler]-->[Uuid: {obj.attributes.temp_handler.uid}|{obj.attributes.temp_handler.name}]
|Name: {obj.name}
|Gender: {obj.gender}
|Age: {obj.age}
|Desc: {obj.desc}
[Level]: {obj.attributes.level}/{obj.attributes.max_level} XP: {obj.attributes.xp}/{obj.attributes.max_xp}
[Abilities]
{obj.abilities}
[Temp]
{get_info_temps(obj)}
[Attributes]
{get_info_attributes(obj)}
[Status]
{get_info_status(obj)}
[Elements]
{get_info_elements(obj)}
[Resistances]
{get_info_resistances(obj)}
'''
    print(data)

def get_info_temps(obj: entities.Character):
    data = ""
    temp : tp.Temp
    if len(obj.attributes.temp_handler.list_temps) > 0:
        for temp in obj.attributes.temp_handler.list_temps:
            data += f"|Status: {temp.status} Type: {temp.typo} Turn: {temp.turn} Time: {temp.time} Value: {temp.value}\n"

    return data



def get_info_resistances(obj: entities.Character) -> str:
    data = ""



    cont = 1
    for chave, valor in obj.attributes.resistances.items():
        reskey = chave + "_Res"
        data += f"|{chave}: {valor}(+{obj.attributes.temp_handler.get_add_bonus(reskey,"add")}/*{obj.attributes.temp_handler.get_mult_bonus(reskey,"mult")})({obj.attributes.resistancesBase[chave]})".ljust(30)

        cont += 1
        if cont > 4:
            data += "\n"
            cont = 1

    return data

def get_info_elements(obj: entities.Character) -> str:
    data = ""

    cont = 1
    for chave, valor in obj.attributes.elements.items():
        data += f"|{chave}: {valor}(+{obj.attributes.temp_handler.get_add_bonus(chave,"add")}/*{obj.attributes.temp_handler.get_mult_bonus(chave,"mult")})".ljust(30)

        cont += 1

        if cont > 4:
            data += "\n"
            cont = 1

    return data



def get_info_attributes(obj: entities.Character) -> str:
    info = obj.attributes.get_all_attr()['attributes']
    data = ""
    cont = 1
    for key,item in enumerate(info.items()):
        chave = item[1]

        data += f"|{chave[0]}({chave[2]}): {chave[1]}(+{chave[3]}/*{chave[4]})".ljust(30)

        cont += 1

        if cont > 4:
            data += "\n"
            cont = 1



    return data


def get_info_status(obj: entities.Character) -> str:
    info = obj.attributes.status.get_info_dict()['status']
    data = ""

    str_just = 30

    cont = 1
    for index,item in enumerate(info.keys()):

        info[item] = trunc(info[item])

        if item == f"max_hp" or item == "max_mp" or item == "max_sp" or item == "max_sanity" or item == "regen_hp" or item == "regen_mp" or item == "regen_sp":
            continue

        st = ''

        if "_" in item:
            st = item.replace("_","").upper()
        else:
            st = item.upper()


        if item == "hp" or item == "mp" or item == "sp":
            max_s = f"max_{item}"
            regen = f"regen_{item}"
            data += f"|{st}: {info[item]}/{info[max_s]}/{info[regen]}(+{obj.attributes.temp_handler.get_add_bonus(info[item],"add")}/*{obj.attributes.temp_handler.get_mult_bonus(info[item],"mult")})".ljust(str_just)
        elif item == "sanity":
            max_s = f"max_{item}"
            data += f"|SY: {info[item]}/{info[max_s]}(+{obj.attributes.temp_handler.get_add_bonus(info[item],"add")}/*{obj.attributes.temp_handler.get_mult_bonus(info[item],"mult")}) ".ljust(str_just)
        else:
            data += f"|{st}: {info[item]}(+{obj.attributes.temp_handler.get_add_bonus(info[item],"add")}/*{obj.attributes.temp_handler.get_mult_bonus(info[item],"mult")}) ".ljust(str_just)


        cont += 1

        if cont > 4:
            data += "\n"
            cont = 1


    return data





def show_info_queue(queue: List[entities.Character]):

    while True:
        print("==" * 40)
        for index, chara in enumerate(queue):
            chara.get_status(index)
        check_id = input("[999 exit] ID: ")

        if check_id == "999":
            break

        if len(check_id) > 0:
            try:
                sid = int(check_id)
                obj = queue[sid]
                obj.attributes.update_attributes()
                show_info_chara(obj)
            except Exception as e:
                print(f"ID: {e}")
        else:
            print("ID does not exist!")


        print("=="*40)



def isCrit(crit_rate):
    rand = random.randint(1,100)

    if rand <= crit_rate:
        return True
    else:
        return False


def check_line(line: str,lines:dict[str,list[str]]) -> bool:

    if line in list(lines.keys()):
        return True
    else:
        return False




def say_line(chara: entities.Character,line_type: str):
    if check_line(line_type,chara.lines):
        line = random.choice(chara.lines[line_type])
        log(Log.CHAT,line,f"[{chara.name}]")


def check_if_attributes_exist(owner: entities.Character):
    if owner.attributes is not None:
        return True
    else:
        return False


