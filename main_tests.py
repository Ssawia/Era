

import json
import classes.entitiesC as entities
import classes.attacks.attackC as atk
import classes.damages.damageTypeC as dmgType
import abstraction
from helpers import show_info_chara



def get_all_status(charas):
    print("="*80)
    for chara in charas:
        chara.get_status()
    print("="*80)



chara_data = open('data/chara/characters.json')
chara_data = json.load(chara_data)["characters"]






flande  = entities.Character(0,chara_data,"Enemy")
remilia = entities.Character(1,chara_data,"Player")
sakuya =  entities.Character(2,chara_data,"Enemy")
remiliaMal =  entities.Character(1,chara_data,"Enemy")

print('\n')


    

queue = [remilia,flande,sakuya,remiliaMal]

while True:
    show_info_chara(remilia)
    atk_id = input("Ataque: ")
    #remilia.attacks[int(atk_id)].doDamage(remilia,queue)
    #remilia.ai.set_behave(remilia,"support")
    remilia.ai.decide_attack(remilia,queue, onEnemy=True)
    get_all_status(queue)


    


































