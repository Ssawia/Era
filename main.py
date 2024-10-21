from __future__ import annotations
import json

from src.classes.entity_prototype import Character,Attributes
from abstraction import get_data_from_id,get_all_json_from_path
from src.classes.battle import Battle
from src.classes.temp.temp_class_handler import Temp




config = json.load(open('config/config.json'))
path_character = config['characters_path']
chara_data: list[dict] = get_all_json_from_path(path_character,'characters')


flandre_data = get_data_from_id(0,chara_data,"[characters]")
remilia_data = get_data_from_id(1,chara_data,"[characters]")
sakuya_data = get_data_from_id(2,chara_data,"[characters]")
artoria_data = get_data_from_id(300,chara_data,"[characters]")

flande = Character(flandre_data,"Enemy")
remilia = Character(remilia_data,"Player")
sakuya =Character(sakuya_data,"Enemy")
artoria = Character(artoria_data,"Player")



#artoria.attributes.add_xp(1000000,artoria)
#helpers.show_info_chara(remilia)

remilia.abilities.append('Phoenix Blessing')

queue : list[Character] = [flande,remilia,sakuya,artoria]


battle =  Battle(queue)
battle.start_battle()



