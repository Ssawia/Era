import uuid
import json
from src.classes.entity_prototype import Character,Attributes,Temp
from abstraction import get_data_from_id,get_all_json_from_path
from src.classes.effects.effect_class_prototype import Burn
import helpers


from dataclasses import dataclass

config = json.load(open('config/config.json'))
path_character = config['characters_path']
chara_data: list[dict] = get_all_json_from_path(path_character,'characters')
flandre_data = get_data_from_id(0,chara_data,"[characters]")
remilia_data = get_data_from_id(1,chara_data,"[characters]")

remilia = Character(remilia_data,"Player",Attributes(remilia_data))
flande = Character(flandre_data,"Enemy",Attributes(flandre_data))





class Events:
    main_func: list = []
    args: list = []
    active = True
    def __init__(self,event_type,name,event_desc,caster):
        self.uid = uuid.uuid4()
        self.event_type = event_type
        self.name = name
        self.event_desc = event_desc
        self.caster = caster

    def start(self,func,args):
        pass

    def process(self):
        pass

    def end(self):
        pass


class OnAttack(Events):


    def __init__(self,event_type,name,event_desc,caster):
        super().__init__(event_type,name,event_desc,caster)



    def start(self,func: list,args: list):
        self.main_func = func
        self.args = args


    def process(self):
        for d_func in self.main_func:
            d_func(args=self.args)












class Listener:
    def __init__(self,listen_type,owner):
        self.listen_type = listen_type
        self.owner = owner



    def listen(self,event):
        pass





class BurnEverything(Listener):
    def __init__(self,listen_type, owner):
        super().__init__(listen_type,owner)


    def listen(self,event : Events):
        if event.caster is not None and isinstance(event.caster,Character) and self.owner != event.caster:
            if self.listen_type == event.event_type:
                caster:Character = event.caster
                print(f"[Event] {event.caster.name} cast the event [{event.event_type}] and activated the Ability [BurnEverything] from {self.owner.name}")

                effect = Burn("burn_effect_01",'Burn','Burn Effect',1,True,True,1,caster)
                caster.effects_handler.add_effects([effect,effect])












class Handler:
    events: list[Events] = []
    events_ids = []
    listeners: list[Listener] = []


    def update_events_id(self):
        if len(self.events) > 0:
            for event in self.events:
                if event.uid not in self.events_ids:
                    self.events_ids.append(event.uid)


    def add_events(self, events: list[Events]):

        for event in events:
            if event.uid not in self.events_ids:
                self.events.append(event)
                self.events_ids.append(event.uid)
            else:
                print("Event Already exist")


    def process_events(self):
        for event in self.events:
            if event.active:
                event.process()

                for listener in self.listeners:
                    listener.listen(event)

                event.active = False



    def remove_events(self):
        new_list: list[Events] = []
        for index,event in enumerate(self.events):
            if event.active:
                new_list.append(event)
                self.events_ids.remove(event.uid)
        self.events = new_list


temp = Temp("vitality","add",1,0,10,True)
temp2 = Temp("vitality","add",1,0,1,True)
temp1 = Temp("hp","mult",1,0,2,True)


flande.attributes.temp_stats.append(temp)
flande.attributes.temp_stats.append(temp2)
flande.attributes.temp_stats.append(temp1)

flande.attributes.update_temp()

flande.attributes.update_attributes()
helpers.show_info_chara(flande)


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
flande.effects_handler.process_effects()
basicHandler.process_events()

basicHandler.remove_events()

#for i in range(2):
    #burnEffect.process_effect()









