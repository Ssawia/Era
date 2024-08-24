import src.classes.entitiesC as entities
import random

def show_info_chara(obj : entities.Character):
    resistances = ""
    elements = ""

    for chave, valor in obj.attributes.resistances.items():
        resistances += f"{chave}: {valor}({obj.attributes.resistancesBase[chave]})|"

    for chave, valor in obj.attributes.elements.items():
        elements += f"{chave}: {valor}|"
    strg = f'''
[{obj.name}]-->[Uuid: {obj.uuid}]
|HP: {obj.attributes.status.hp}/{obj.attributes.status.maxHp}({obj.attributes.status.regenHp}) |SP: {obj.attributes.status.sp}/{obj.attributes.status.maxSp}({obj.attributes.status.regenSp}) |MP: {obj.attributes.status.mp}/{obj.attributes.status.maxMp}({obj.attributes.status.regenMp}) |SY: {obj.attributes.status.sanity}/{obj.attributes.status.maxSanity}
|ATK: {obj.attributes.status.atk} |ATKM: {obj.attributes.status.atkM} |DEF: {obj.attributes.status.df} |DEFM: {obj.attributes.status.dfM} |RES: {obj.attributes.status.res} |RESM: {obj.attributes.status.resM} 
|DGE: {obj.attributes.status.dodge} |SPD: {obj.attributes.status.spd} |CRIT: {obj.attributes.status.crit:.1f}% |CRITD: {obj.attributes.status.maxCrit:.1f}% |ITEM: {obj.attributes.status.item}% |LOAD: {obj.attributes.status.load}/kg

[Elements]: {elements}
[Resistances]: {resistances}
'''
    print(strg)


def isCrit(crit_rate):
    rand = random.randint(1,100)

    if rand <= crit_rate:
        return True
    else:
        return False


