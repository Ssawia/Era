

import json
import classes.entitiesC as entities
import classes.attacks.attackC as atk
import classes.damages.damageTypeC as dmgType


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


while True:
    atk_id = input("Ataque: ")
    remilia.attacks[int(atk_id)].doDamage(remilia,[remilia,flande,sakuya,remiliaMal])
    get_all_status([flande,sakuya,remiliaMal])




























