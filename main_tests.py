

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





def show_info_chara(obj : entities.Character):
    resistances = ""
    elements = ""

    for chave, valor in obj.attributes.resistances.items():
        resistances += f"{chave}: {valor}({obj.attributes.resistancesBase[chave]})|"

    for chave, valor in obj.attributes.elements.items():
        elements += f"{chave}: {valor}|"
    strg = f'''
[{obj.name}] 
|HP: {obj.attributes.status.hp}/{obj.attributes.status.maxHp}({obj.attributes.status.regenHp}) |SP: {obj.attributes.status.sp}/{obj.attributes.status.maxSp}({obj.attributes.status.regenSp}) |MP: {obj.attributes.status.mp}/{obj.attributes.status.maxMp}({obj.attributes.status.regenMp}) |SY: {obj.attributes.status.sanity}/{obj.attributes.status.maxSanity}
|ATK: {obj.attributes.status.atk} |ATKM: {obj.attributes.status.atkM} |DEF: {obj.attributes.status.df} |DEFM: {obj.attributes.status.dfM} |RES: {obj.attributes.status.res} |RESM: {obj.attributes.status.resM} 
|DGE: {obj.attributes.status.dodge} |SPD: {obj.attributes.status.spd} |CRIT: {obj.attributes.status.crit:.1f}% |CRITD: {obj.attributes.status.maxCrit:.1f}% |ITEM: {obj.attributes.status.item}% |LOAD: {obj.attributes.status.load}/kg
[Elements]: {elements}
[Resistances]: {resistances}
'''

    print(strg)

while True:
    show_info_chara(remilia)
    atk_id = input("Ataque: ")
    remilia.attacks[int(atk_id)].doDamage(remilia,[remilia,flande,sakuya,remiliaMal])
    print(flande.effects)
    get_all_status([flande,sakuya,remiliaMal])
    


































