

import json
import classes.entitiesC as entities
import classes.attackC as atk
import classes.damageTypeC as dmgType


def get_all_status(charas):
    print("=============================================")
    for chara in charas:
        chara.get_status()
    print("=============================================")



chara_data = open('data/chara/characters.json')
chara_data = json.load(chara_data)["characters"]



flande  = entities.Character(chara_data[0],"Enemy")
remilia = entities.Character(chara_data[1],"Player")
sakuya =  entities.Character(chara_data[2],"Player")



print(remilia.attacks[1].doDamage(remilia,[flande,sakuya]))


get_all_status([flande,sakuya])

print(remilia.attacks[3].doDamage(remilia,[flande,sakuya]))
remilia.get_status()

get_all_status([flande,sakuya])



















