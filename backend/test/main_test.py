from src.classes.entity_prototype import Character,Attributes
from abstraction import get_data_from_id,get_all_json_from_path
from src.classes.battle import Battle
from src.classes.temp.temp_class_handler import Temp
import json


config = json.load(open('config/config.json'))
path_character = config['characters_path']
chara_data: list[dict] = get_all_json_from_path(path_character,'characters')


flandre_data = get_data_from_id(0,chara_data,"[characters]")
remilia_data = get_data_from_id(1,chara_data,"[characters]")

flande = Character(flandre_data,"Enemy")
remilia = Character(remilia_data,"Player")

queue : list[Character] = [flande,remilia]





battle =  Battle(queue)
battle.start_battle()











def test_can_create_character():
    chara_data = open('data/chara/characters.json')
    chara_data = json.load(chara_data)["characters"]
    chara = Character(0,chara_data,"Enemy")
    assert chara.get_status(0) == True


def test_when_create_character_init_the_attacks():
    chara_data = open('data/chara/characters.json')
    chara_data = json.load(chara_data)["characters"]
    chara = Character(0,chara_data,"Enemy")
    assert chara.attacks[0].name == "Punch"

