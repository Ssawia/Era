import importlib
import json
from typing import List
import src.classes.entitiesC as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.attacks.attackC as Attack
import os

config = json.load(open('config/config.json'))


config_data = config["damage_data"]
class_path = config['class_path']
path_attacks = config['path_attacks']





def get_elements(elementType : str):
    elements_final = []
    elements = json.load(open(config_data))

    if elementType == "Res":
        for element in elements['DamagesType']:
            if element['name'] not in elements_final and element['type'] != "healing":
                elements_final.append({element['name']:element['Rscale']})
    elif elementType == "Atk":
        for element in elements['DamagesType']:
            if element['name'] not in elements_final and element['type'] != "healing":
                elements_final.append({element['name']:element['Ascale']})        
    
    return elements_final

    


#carregar a classe baseado no local onde ela está
def str_to_class(type_class : str, file : str, classname : str, ):
    module = importlib.import_module(f'{class_path}.{type_class}.{file}')
    abclass = getattr(module, classname)
    return abclass


def getDamageTypeClass(data : list, damage_data : dict, damages : list):
    dtypeList: List[dmgType.DamageType] = []

    dtype : dmgType.DamageType
    i = 0

    atk = 0
    heal = 0
    #Melhorar essa merda, pro futuro quando tiver mais tipo de dano não virar um yandere simulator
    for c in data:
        if 'atk' in damages[i].keys():
            atk = damages[i]['atk']
        if 'heal' in damages[i].keys():
            heal = damages[i]['heal']

        typeDmg = next((sub for sub in damage_data if sub['_id'] == c))


        dtype = str_to_class(typeDmg['classType'],typeDmg['file'],typeDmg['className'])(file=typeDmg['file'],name=typeDmg['name'],desc=typeDmg['desc'],atk=atk,heal=heal,defType=typeDmg['defType'])
        dtypeList.append(dtype)
        i += 1
    
    return dtypeList


def getAttackClass(data : list):

    damage_data = open(config_data)
    damage_data = json.load(damage_data)["DamagesType"]
    attacks_list = []


    attacks_data = []

    for file_name in [file for file in os.listdir(path_attacks) if file.endswith('.json')]:
        with open(path_attacks + file_name) as json_file:
            json_data = json.load(json_file)['attacks']
            attacks_data.extend(json_data)

    for c in data:

        damagetypes: List[dmgType.DamageType] = []
        basicAttack: Attack.Attack 


        attack = next((sub for sub in attacks_data if sub['_id'] == c))
        damagetypes = getDamageTypeClass(attack['type'], damage_data, attack['damage'])



        #melhorar essa merda kkkkkkkk
        basicAttack  = str_to_class(attack['classType'],attack['file'],attack['className'])(
            _id = attack['_id'],
            _class =attack['className'],
            name=attack['name'],
            desc=attack['desc'],
            target=attack['target'],
            targetLimit=attack['target-limit'],
            intent=attack['intent'],
            damage=attack['damage'],
            cost= attack['cost'],
            hits = attack['hits'],
            dmgType = damagetypes)
        attacks_list.append(basicAttack)
    
    return attacks_list








