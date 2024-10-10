from __future__ import annotations
import src.classes.entity_prototype as entities
import random
from typing import List

def show_info_chara(obj : entities.Character):
    resistances = ""
    elements = ""

    for chave, valor in obj.attributes.resistances.items():
        resistances += f"{chave}: {valor}({obj.attributes.resistancesBase[chave]})|"

    for chave, valor in obj.attributes.elements.items():
        elements += f"{chave}: {valor}|"
    strg = f'''
[{obj.name}]-->[Uuid: {obj.uuid}]
[Level]: {obj.attributes.level}/{obj.attributes.max_level} XP: {obj.attributes.xp}/{obj.attributes.max_xp}
[Attributes]
|Vitality: {obj.attributes.vitality}(+{obj.attributes.temp_handler.get_add_bonus("vitality","add")}/*{obj.attributes.temp_handler.get_mult_bonus("vitality","mult")})
|Constitution: {obj.attributes.constitution}(+{obj.attributes.temp_handler.get_add_bonus("constitution","add")}/*{obj.attributes.temp_handler.get_mult_bonus("constitution","mult")})
|Strength: {obj.attributes.strength}(+{obj.attributes.temp_handler.get_add_bonus("strength","add")}/*{obj.attributes.temp_handler.get_mult_bonus("strength","mult")})
|Fortitude: {obj.attributes.fortitude}(+{obj.attributes.temp_handler.get_add_bonus("fortitude","add")}/*{obj.attributes.temp_handler.get_mult_bonus("fortitude","mult")})
|Attunement: {obj.attributes.attunement}(+{obj.attributes.temp_handler.get_add_bonus("attunement","add")}/*{obj.attributes.temp_handler.get_mult_bonus("attunement","mult")})
|Intelligence: {obj.attributes.intelligence}(+{obj.attributes.temp_handler.get_add_bonus("intelligence","add")}/*{obj.attributes.temp_handler.get_mult_bonus("intelligence","mult")})
|Will: {obj.attributes.will}(+{obj.attributes.temp_handler.get_add_bonus("will","add")}/*{obj.attributes.temp_handler.get_mult_bonus("will","mult")})
|Faith: {obj.attributes.faith}(+{obj.attributes.temp_handler.get_add_bonus("faith","add")}/*{obj.attributes.temp_handler.get_mult_bonus("faith","mult")})
|Arcane: {obj.attributes.arcane}(+{obj.attributes.temp_handler.get_add_bonus("arcane","add")}/*{obj.attributes.temp_handler.get_mult_bonus("arcane","mult")})
|Dexterity: {obj.attributes.dexterity}(+{obj.attributes.temp_handler.get_add_bonus("dexterity","add")}/*{obj.attributes.temp_handler.get_mult_bonus("dexterity","mult")})
|Fortune: {obj.attributes.fortune}(+{obj.attributes.temp_handler.get_add_bonus("fortune","add")}/*{obj.attributes.temp_handler.get_mult_bonus("fortune","mult")})
[Status]
|HP: {obj.attributes.status.hp}/{obj.attributes.status.maxHp}({obj.attributes.status.regenHp}) |SP: {obj.attributes.status.sp}/{obj.attributes.status.maxSp}({obj.attributes.status.regenSp}) |MP: {obj.attributes.status.mp}/{obj.attributes.status.maxMp}({obj.attributes.status.regenMp}) |SY: {obj.attributes.status.sanity}/{obj.attributes.status.maxSanity}
|ATK: {obj.attributes.status.atk} |ATKM: {obj.attributes.status.atkM} |DEF: {obj.attributes.status.df} |DEFM: {obj.attributes.status.dfM} |RES: {obj.attributes.status.res} |RESM: {obj.attributes.status.resM} 
|DGE: {obj.attributes.status.dodge} |SPD: {obj.attributes.status.spd} |CRIT: {obj.attributes.status.crit:.1f}% |CRITD: {obj.attributes.status.maxCrit:.1f}% |ITEM: {obj.attributes.status.item}% |LOAD: {obj.attributes.status.load}/kg

[Elements]: {elements}
[Resistances]: {resistances}
'''
    print(strg)




def show_info_queue(queue: List[entities.Character]):
    print("=="*40)
    for index,chara in  enumerate(queue):
            chara.get_status(index)
    
    msg = input('More Informations ? y n :')

    check = False

    if msg == "y":
        check = True
    
    while check:
        check_id = input("[999 exit] ID: ")

        if check_id == "999":
            break

        if len(check_id) > 0:
            try:
                sid = int(check_id)
                show_info_chara(queue[sid])
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
        print(f"{chara.name}: {line}")


def check_if_attributes_exist(owner: entities.Character):
    if owner.attributes is not None:
        return True
    else:
        return False


