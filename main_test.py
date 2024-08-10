import classes.entitiesC as ent
import json

Character = ent.Character

def test_can_create_character():
    chara_data = open('data/chara/characters.json')
    chara_data = json.load(chara_data)["characters"]
    chara = Character(0,chara_data,"Enemy")
    assert chara.get_status() == True


def test_when_create_character_init_the_attacks():
    chara_data = open('data/chara/characters.json')
    chara_data = json.load(chara_data)["characters"]
    chara = Character(0,chara_data,"Enemy")
    assert chara.attacks[0].name == "Punch"

