from __future__ import annotations
import uuid
import src.classes.listerners.listerner_class as ltn
import src.classes.entity_prototype as ch

class Event:
    
    def __init__(self,event_type,caster, target = None):
        self.active = True
        self.uid = uuid.uuid4()
        self.event_type: str = event_type
        self.caster: ch.Character = caster
        self.target: ch.Character = target

class On_Start_Attack(Event):
    def __init__(self, event_type, caster, target=None, attack = None):
        super().__init__(event_type, caster, target)
        self.attack = attack

class On_Damage(Event):
    def __init__(self, event_type, caster, target=None, dmg_obj = None, damage = 0):
        super().__init__(event_type, caster, target)
        self.dmg_obj = dmg_obj
        self.damage = damage


class Handler:
    events: list[Event] = []
    events_ids = []
    listeners: list[ltn.Listener] = []


    def update_events_id(self):
        if len(self.events) > 0:
            for event in self.events:
                if event.uid not in self.events_ids:
                    self.events_ids.append(event.uid)


    def add_events(self, events: list[Event]):

        for event in events:
            if event.uid not in self.events_ids and event is not None:
                self.events.append(event)
                self.events_ids.append(event.uid)
            else:
                print("Event Already exist")


    def process_events(self, type):
        event: Event
        for event in self.events:
            if event.active and event.event_type == type:
                for listener in self.listeners:
                    result = listener.listen(event)

                event.active = False
        
        self.remove_events()
    
    
    def remove_listeners(self):
        new_list: list[ltn.Listener] = []
        
        for index,listerner in enumerate(self.listeners):
            if listerner.active:
                new_list.append(listerner)
        self.listeners = new_list



    def remove_events(self):
        new_list: list[Event] = []
        for index,event in enumerate(self.events):
            if event.active:
                new_list.append(event)
                self.events_ids.remove(event.uid)
        self.events = new_list


