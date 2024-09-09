from __future__ import annotations
import importlib
import json
import src.classes.entitiesC as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.attacks.attackC as Attack
import os


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





def get_elements(elementType : str):
    elements_final = []
    elements = get_all_json_from_path(damages_path,"DamagesType")
    

    if elementType == "Res":
        for element in elements:
            if element['name'] not in elements_final and element['type'] != "healing":
                elements_final.append({element['name']:element['Rscale']})
    elif elementType == "Atk":
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

    atk = 0
    heal = 0
    #Melhorar essa merda, pro futuro quando tiver mais tipo de dano não virar um yandere simulator

    for c in data:
        if 'atk' in damages[i].keys():
            atk = damages[i]['atk']
        if 'heal' in damages[i].keys():
            heal = damages[i]['heal']

        typeDmg = get_data_from_id(c,damage_data,"[damage]")


        dtype = str_to_class(typeDmg['classType'],typeDmg['file'],typeDmg['className'])(file=typeDmg['file'],name=typeDmg['name'],desc=typeDmg['desc'],atk=atk,heal=heal,defType=typeDmg['defType'])
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
    data = {}

    if check_ids_in_list_dict(sid,data_list):
        data = next((sub for sub in data_list if sub['_id'] == sid))
    else:
        print(f"{id_type}[ID: {sid}] does not exist, using [ID: 0]")
        data = next((sub for sub in data_list if sub['_id'] == 0))

    return data


def getAttackClass(data : list[int]) -> list[Attack.Attack]:


    attacks_list = []

    


    for c in data:

        damagetypes: list[dmgType.DamageType] = []
        basicAttack: Attack.Attack 

        

        
        attack = get_data_from_id(c,attacks_data,"[attack]")

    
        damagetypes = getDamageTypeClass(attack['type'], attack['damage'])



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








