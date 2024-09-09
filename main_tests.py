

import json
import src.classes.entitiesC as entities
import src.classes.attacks.attackC as atk
import src.classes.damages.damageTypeC as dmgType
import abstraction
from helpers import show_info_chara
import os
from typing import List



def get_all_status(charas):
    print("="*80)
    for chara in charas:
        chara.get_status()
    print("="*80)


config = json.load(open('config/config.json'))



chara_data = open(config["character_data"])
chara_data = json.load(chara_data)["characters"]






flande  = entities.Character(0,chara_data,"Enemy")
remilia = entities.Character(1,chara_data,"Player")
sakuya =  entities.Character(2,chara_data,"Enemy")
remiliaMal =  entities.Character(1,chara_data,"Enemy")


queue: List[entities.Character] | None = None 
queue = [remilia,flande,sakuya,remiliaMal]

queue.sort(key=lambda x: x.ai.typeAi )

que



for i,chara in enumerate(queue):
   print(f"[{i}][{chara.ai.typeAi}]{chara.name}")





'''while True:
    show_info_chara(remilia)
    atk_id = input("Ataque: ")
    #remilia.attacks[int(atk_id)].doDamage(remilia,queue)
    #remilia.ai.set_behave(remilia,"support")
    remilia.ai.decide_attack(remilia,queue, onEnemy=True)
    get_all_status(queue)'''










































