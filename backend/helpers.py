from __future__ import annotations

from math import trunc
from tkinter.ttk import Treeview

import src.classes.entity_prototype as entities
import src.classes.temps.temp_class_handler as tp
import src.classes.effects.effect_class as eff
import random
from typing import List
from enum import Enum
import json

config = json.load(open('config/config.json'))
is_debug = config['debug']
is_event = config['event']

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
        msg = f"[{typ.value}{typ.name}{reset}]{append}{message}"
        print(msg)
    else:
        msg = ''
        print(msg,end="")
    
    if is_event and typ == Log.EVENT:
        msg = f"[{typ.value}{typ.name}{reset}]{append}{message}"
        print(msg)
    else:
        msg = ''
        print(msg,end="")

    if typ != Log.DEBUG and typ != Log.EVENT:
        msg = f"[{typ.value}{typ.name}{reset}]{append}{message}"
        print(msg)


def line(word: str = "=",number: int = 120):
    print(f"{word}"*number)





def get_potencial_string(number: float) -> str:
    potencial = {
        0.00: "G",
        0.05: "F",
        0.1: "E",
        0.15: "D",
        0.2: "C",
        0.25: "B",
        0.3: "A",
        0.35: "S",
        0.4: "EX"
    }

    if 0.0 <= number <= 0.4:
        return potencial[number]
    else:
        return potencial[0.0]


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
[Effects]
{get_info_effects(obj)}
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
[Debug]
{get_debug_info(obj)}
'''
    print(data)

def get_debug_info(obj: entities.Character):
    data = ""
    
    #HP
    data += f"\n[hp]\n->|hp: vitality({obj.attributes.vitality})*10*potencial_vitality({obj.attributes.potential.vitality})={obj.attributes.vitality * 10 * obj.attributes.potential.vitality}"

    #ATK
    data += f"\n[atk]\n->|atk: strength({obj.attributes.strength})*potencial_strenght({obj.attributes.potential.strength})={obj.attributes.strength*obj.attributes.potential.strength}"
    
    #ATKM
    atm_bonus = ""
    if (obj.attributes.faith * obj.attributes.potential.faith) >= (obj.attributes.arcane * obj.attributes.potential.arcane):
        pt_atkm = (obj.attributes.potential.intelligence + obj.attributes.potential.faith) / 2
        atm_bonus = ["faith", obj.attributes.potential.faith]
    else:
        pt_atkm = (obj.attributes.potential.intelligence + obj.attributes.potential.arcane) / 2
        atm_bonus = ["arcane", obj.attributes.potential.arcane]
    
    data +=  f"\n[atk_m]\n->|potencial_intelligence({obj.attributes.potential.intelligence})+potencial_{atm_bonus[0]}({atm_bonus[1]})/2 = {pt_atkm}\n->|atkm: intelligence({obj.attributes.intelligence})*{pt_atkm}={obj.attributes.intelligence*pt_atkm}"

    return "None"

def get_info_effects(obj: entities.Character):
    data = ""
    effect : eff.Effect
    if len(obj.effects_handler.effects) > 0:
        for effect in obj.effects_handler.effects:
            data += f"|Active: {effect.active} Name: {effect.name} Turn: {effect.turn} Stacks: {effect.stacks} HasTemp: {effect.has_temp}\n-> {effect.desc}\n"
    return data

def get_info_temps(obj: entities.Character):
    data = ""
    temp : tp.Temp
    if len(obj.attributes.temp_handler.list_temps) > 0:
        for temp in obj.attributes.temp_handler.list_temps:
            data += f"|Status: {temp.status} Type: {temp.typo} Turn: {temp.turn} Time: {temp.time} Value: {temp.value} Flag: {temp.active_flag}\n"

    return data



def get_info_resistances(obj: entities.Character) -> str:
    data = ""



    cont = 1
    for chave, valor in obj.attributes.resistances.items():
        reskey = chave + "_Res"
        data += f"|{chave}: {valor}(+{obj.attributes.temp_handler.get_add_bonus(reskey,"add")}/*{obj.attributes.temp_handler.get_mult_bonus(reskey,"mult")})".ljust(30)

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
    text = ""
    cont = 1
    for data in info.keys():
        
        text += f"|{info[data][0]}({info[data][2]}): {info[data][1]}(+{info[data][3]}/*{info[data][4]})".ljust(30)

        cont += 1

        if cont > 4:
            text += "\n"
            cont = 1



    return text


def get_info_status(obj: entities.Character) -> str:
    info = obj.attributes.status.get_info_dict()['status']
    data = ""

    str_just = 30
    cont = 1
    for index,item in enumerate(info.keys()):

        if not item == "spd":
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
            data += f"|{st}: {info[item]}/{info[max_s]}/{info[regen]}(+{obj.attributes.temp_handler.get_add_bonus(item,"add")}/*{obj.attributes.temp_handler.get_mult_bonus(item,"mult")})".ljust(str_just)
        elif item == "sanity":
            data += f"|SY: {info[item]}%(+{obj.attributes.temp_handler.get_add_bonus(item,"add")}/*{obj.attributes.temp_handler.get_mult_bonus(item,"mult")}) ".ljust(str_just)
        elif item == "res" or item == "res_m":
            data += f"|{st}: {info[item]}%(+{obj.attributes.temp_handler.get_add_bonus(item,"add")}/*{obj.attributes.temp_handler.get_mult_bonus(item,"mult")}) ".ljust(str_just)
        else:
            data += f"|{st}: {info[item]}(+{obj.attributes.temp_handler.get_add_bonus(item,"add")}/*{obj.attributes.temp_handler.get_mult_bonus(item,"mult")}) ".ljust(str_just)


        cont += 1

        if cont > 4:
            data += "\n"
            cont = 1


    return data



def check_cost(chara: entities.Character, attack_id: int, quantity: int = 1) -> bool:

    costs = chara.attacks[attack_id].cost
    can_attack = False

    info_attack = ''
    attack_name = chara.attacks[attack_id].name

    for cost in costs:
        if cost == "mp" and chara.attributes.status.mp >= costs[cost]:
            chara.attributes.status.mp -= costs[cost]
            info_attack += f"MP: {costs[cost]} "
            can_attack = True

        elif cost == "sp" and chara.attributes.status.sp >= costs[cost]:
            chara.attributes.status.sp -= costs[cost]
            info_attack += f"SP: {costs[cost]} "
            can_attack = True

        elif cost == "hp" and chara.attributes.status.hp >= costs[cost]:
            chara.attributes.status.hp -= costs[cost]
            info_attack += f"HP: {costs[cost]} "
            can_attack = True
        else:
            log(Log.WARNING,f"Sem {cost} para o ataque")
            can_attack = False

    log(Log.INFO, info_attack,f"[{chara.name}][Attack][{attack_name}]")

    return can_attack










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


def say_string(chara: entities.Character, line):
    log(Log.CHAT,line,f"[{chara.name}] ")


def say_line(chara: entities.Character,line_type: str):
    if check_line(line_type,chara.lines):
        line = random.choice(chara.lines[line_type])
        log(Log.CHAT,line,f"[{chara.name}]")


def check_if_attributes_exist(owner: entities.Character):
    if owner.attributes is not None:
        return True
    else:
        return False


