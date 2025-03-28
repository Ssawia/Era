import uuid
import json
from src.classes.entity_prototype import Character,Attributes
from src.classes.temp.temp_class_handler import Temp
from abstraction import get_data_from_id,get_all_json_from_path
from backend.src.classes.effects.effect_class import Burn
import helpers
from helpers import log,Log


from dataclasses import dataclass

config = json.load(open('config/config.json'))
path_character = config['characters_path']
chara_data: list[dict] = get_all_json_from_path(path_character,'characters')
flandre_data = get_data_from_id(0,chara_data,"[characters]")
remilia_data = get_data_from_id(1,chara_data,"[characters]")

remilia = Character(remilia_data,"Player")
flande = Character(flandre_data,"Enemy")





































queue = [flande,remilia]


# Evento 1 criado, ataque usando select para o Player
atkEvent = OnAttack('OnAttack','Attack_1',"Attack basico",remilia)
func = remilia.attacks[0].doDamage
atkEvent.start([func],[remilia,queue,False])

#Evento 2 criado, ataque usando a IA para selecionar
atkEvent1 = OnAttack('OnAttack','Attack_1',"Attack IA",flande)
func1 = flande.ai.decide_attack
atkEvent1.start([func1],[flande,queue,True])


burn = BurnEverything("OnAttack",remilia)


basicHandler = Handler()


basicHandler.listeners.append(burn)


basicHandler.add_events([atkEvent,atkEvent1])
basicHandler.process_events()
flande.effects_handler.process_effects()


helpers.show_info_chara(remilia)

basicHandler.remove_events()

#for i in range(2):
    #burnEffect.process_effect()










