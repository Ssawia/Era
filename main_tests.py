

import json
import classes.entitiesC as entities
import classes.attacks.attackC as atk
import classes.damages.damageTypeC as dmgType
import abstraction


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


resistances = ""
elements = ""


for chave, valor in flande.attributes.resistances.items():
    resistances += f"|{chave}: {valor}({flande.attributes.resistancesBase[chave]}) \n"


for chave, valor in flande.attributes.elements.items():
    elements += f"|{chave}: {valor} \n"


strg = f'''
[{flande.name}] 
|HP: {flande.attributes.status.hp}/{flande.attributes.status.maxHp}({flande.attributes.status.regenHp})
|SP: {flande.attributes.status.sp}/{flande.attributes.status.maxSp}({flande.attributes.status.regenSp})
|MP: {flande.attributes.status.mp}/{flande.attributes.status.maxMp}({flande.attributes.status.regenMp})
|SY: {flande.attributes.status.sanity}/{flande.attributes.status.maxSanity}
|ATK: {flande.attributes.status.atk}                                                                                                           
|DEF: {flande.attributes.status.df}
|RES: {flande.attributes.status.res}
|ATKM: {flande.attributes.status.atkM}
|DEFM: {flande.attributes.status.dfM}
|RESM: {flande.attributes.status.resM}
|DGE: {flande.attributes.status.dodge}
|SPD: {flande.attributes.status.spd}
|CRIT: {flande.attributes.status.crit:.1f}%
|CRITD: {flande.attributes.status.maxCrit:.1f}%
|ITEM: {flande.attributes.status.item}%
|LOAD: {flande.attributes.status.load}/kg
\n
[Elements]
{elements}
[Resistances]
{resistances}
'''































