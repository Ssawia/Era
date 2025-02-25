from __future__ import annotations
import importlib
import json
import src.classes.entity_prototype as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.attacks.attackC as atk
import os

Attack = atk.Attack

config = json.load(open('config/config.json'))



class_path = config['class_path']
path_attacks = config['path_attacks']
characters_path = config['characters_path']
damages_path = config['damage_data']

def get_all_json_from_path(init_path : str,path_type : str) -> list[dict]:
    data = []

    for file_name in [file for file in os.listdir(init_path) if file.endswith('.json')]:
        with open(init_path + file_name) as json_file:
            json_data = json.load(json_file)[path_type]
            data.extend(json_data)
    return data    


attacks_data = get_all_json_from_path(path_attacks,'attacks')





def get_elements():
    elements_final = []
    elements = get_all_json_from_path(damages_path,"DamagesType")
    
    
    for element in elements:
        if element['name'] not in elements_final and element['type'] != "healing":
            elements_final.append({element['name']:element['Ascale']})        
    
    return elements_final

    


#carregar a classe baseado no local onde ela está
def str_to_class(type_class : str, file : str, classname : str, ):
    module = importlib.import_module(f'{class_path}.{type_class}.{file}')
    abclass = getattr(module, classname)
    return abclass


def getDamageTypeClass(data : list, damages : list):
    dtypeList: list[dmgType.DamageType] = []

    dtype : dmgType.DamageType
    i = 0


    damage_data = get_all_json_from_path(damages_path,"DamagesType")

    min_atk = 0
    max_atk = 0
    min_heal = 0
    max_heal = 0
    heal = 0
    #Melhorar essa merda, pro futuro quando tiver mais tipo de dano não virar um yandere simulator

    for c in data:
        if 'atk' in damages[i].keys():
            min_atk = damages[i]['atk'][0]
            max_atk = damages[i]['atk'][1]
        if 'heal' in damages[i].keys():
            min_heal = damages[i]['heal']
            max_heal = damages[i]['heal']

        type_dmg = get_data_from_id(c,damage_data,"[damage]")


        dtype = str_to_class(type_dmg['classType'],type_dmg['file'],type_dmg['className'])(file=type_dmg['file'],name=type_dmg['name'],desc=type_dmg['desc'],min_atk=min_atk,max_atk=max_atk,min_heal=min_heal,max_heal=max_heal,defType=type_dmg['defType'])
        dtypeList.append(dtype)
        i += 1
    
    return dtypeList





def check_ids_in_list_dict(sid: int,data_list: list[dict]):
    ids = [ids['_id'] for ids in data_list]

    if sid in ids:
        return True
    else:
        return False



def get_data_from_id(sid: int, data_list: list[dict],id_type:str):
    """ Checks if the id exists within the list with dicts \n 
        Returns a dict
    """
    data = {}

    if check_ids_in_list_dict(sid,data_list):
        data = next((sub for sub in data_list if sub['_id'] == sid))
    else:
        print(f"{id_type}[ID: {sid}] does not exist, using [ID: 0]")
        data = next((sub for sub in data_list if sub['_id'] == 0))

    return data


def get_attack_class(data : list[int]) -> list[Attack]:

    attacks_list: list[Attack] = []

    for c in data:
        basic_attack: atk.Attack
        
        attack = get_data_from_id(c,attacks_data,"[attack]")
        damages_type = getDamageTypeClass(attack['type'], attack['damage'])


        basic_attack  = str_to_class(attack['classType'],attack['file'],attack['className'])(attack,damages_type)
        attacks_list.append(basic_attack)
    
    return attacks_list








