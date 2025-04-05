from __future__ import annotations
import uuid
import src.classes.entity.character as etc
import src.classes.events.event_class_prototype as evt
import src.classes.temps.temp_class_handler as tmp
import helpers
import random
import abstraction

log = helpers.log
Log = helpers.Log



class Listener:
    def __init__(self,name,desc,listen_type,owner):
        self.active = True
        self.uid = uuid.uuid4()
        self.name = name
        self.desc = desc
        self.listen_type = listen_type
        self.owner: etc.Character = owner
        

    def listen(self,event):
        pass

    def end(self):
        pass


class PhoenixBlessing(Listener):
    def __init__(self, name, desc, listen_type, owner):
        super().__init__(name, desc, listen_type ,owner)
    
    def listen(self, event: evt.Event):
        if event.caster is not None and isinstance(event.caster, etc.Character) and self.owner == event.caster:
            if self.listen_type == event.event_type:
                log(Log.EVENT, f" Evento {self.listen_type} de {event.caster.name} escutado por {self.name} de {self.owner.name}", f"[Listener][{self.owner.name}]")
                
                # Codigo
                tmp_buff = tmp.Temp("Fire Feather A-","Fire","add",1,0,1,True,True,False,"")
                self.owner.attributes.temp_handler.add_temp([tmp_buff])
                # .....
                # Codigo

                self.active = False
                return True

class FateManipulation(Listener):
    def __init__(self, name, desc, listen_type, owner):
        super().__init__(name, desc, listen_type ,owner)
    
    def listen(self,event: evt.On_Damage):
        if self.owner == event.target:
            if self.listen_type == event.event_type:
                #log(Log.EVENT, f" Evento {self.listen_type} feito por {event.caster.name} escutado por {self.name} de {self.owner.name}", f"[Listener][{self.owner.name}]")

                log(Log.EVENT, f" Ability {self.name} from {self.owner.name} actived.", f"[{self.owner.name}][{event.event_type.upper()}]")
    

                helpers.say_string(self.owner, self.desc)
                base_perc = 10 + self.owner.attributes.temp_handler.get_add_bonus(self.name, "add")

                num = random.randint(1,100)
                if num <= base_perc:
                    log(Log.EVENT, f" {self.owner.name} tried to manipulate fate, and I managed to completely ignore the damage", f"[num: {num}/{base_perc}]")
                    damage = event.damage
                    self.owner.attributes.status.hp += damage

                    temp = abstraction.get_temp_from_id(3,"")
                    self.owner.attributes.temp_handler.add_temp([temp])

                else:
                    log(Log.EVENT, f" {self.owner.name} could not manipulate destiny.", f"[num: {num}]")

                return True


            


            



class BurnEverything(Listener):
    def __init__(self,listen_type, owner):
        super().__init__(listen_type,owner)


    def listen(self,event : evt.Event):
        if event.caster is not None and isinstance(event.caster,etc.Character) and self.owner != event.caster:
            if self.listen_type == event.event_type:
                caster:etc.Character = event.caster
                #log(Log.EVENT, f"{event.caster.name} cast the event [{event.event_type}] and activated the Ability [BurnEverything] from {self.owner.name}")

                temp = tmp.Temp("faith", "add", 1, 0, 10, True,True,False,caster.uuid)
                self.owner.attributes.temp_handler.add_temp([temp])

                #effect = Burn("burn_effect_01",'Burn','Burn Effect',1,True,True,1,caster,True,[temp],self.owner)
                #caster.effects_handler.add_effects([effect])
                self.end()