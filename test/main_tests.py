

import json
import src.classes.entitiesC as entities
import src.classes.attacks.attackC as atk
import src.classes.damages.damageTypeC as dmgType
import abstraction
from helpers import show_info_chara
import os



def get_all_status(charas):
    print("="*80)
    for chara in charas:
        chara.get_status()
    print("="*80)



chara_data = open('data/chara/characters.json')
chara_data = json.load(chara_data)["characters"]






'''flande  = entities.Character(0,chara_data,"Enemy")
remilia = entities.Character(1,chara_data,"Player")
sakuya =  entities.Character(2,chara_data,"Enemy")
remiliaMal =  entities.Character(1,chara_data,"Enemy")

print('\n')

asd = []

for c in range(1000):
    asd.append(entities.Character(0,chara_data,"Enemy"))

    

queue = [remilia,flande,sakuya,remiliaMal]

while True:
    show_info_chara(remilia)
    atk_id = input("Ataque: ")
    #remilia.attacks[int(atk_id)].doDamage(remilia,queue)
    #remilia.ai.set_behave(remilia,"support")
    remilia.ai.decide_attack(remilia,queue, onEnemy=True)
    get_all_status(queue)'''



path_to_json = 'data/attacks/'
all_attacks = []

for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
  with open(path_to_json + file_name) as json_file:
    data = json.load(json_file)['Attacks']
    all_attacks.extend(data)



attack = next((sub for sub in all_attacks if sub['_id'] == 1))

print(attack)





































