

import json
import classes.entitiesC as entities
import classes.attackC as atk
import classes.damageTypeC as dmgType


def get_all_status(charas):
    print("="*80)
    for chara in charas:
        chara.get_status()
    print("="*80)



chara_data = open('data/chara/characters.json')
chara_data = json.load(chara_data)["characters"]



flande  = entities.Character(chara_data[0],"Enemy")
remilia = entities.Character(chara_data[1],"Player")
sakuya =  entities.Character(chara_data[2],"Enemy")
remiliaMal =  entities.Character(chara_data[1],"Enemy")



remilia.attacks[3].doDamage(remilia,[remilia,flande,sakuya,remiliaMal])


get_all_status([flande,sakuya])




















