from __future__ import annotations
from src.classes.effects.effect_handler_class_prototype import EffectHandler
from src.classes.ia_class_prototype import Ai
from math import trunc
from dataclasses import dataclass
import uuid
import random
import helpers
from helpers import log,Log
import abstraction
import src.classes.damages.damageTypeC as damageTypes
import src.classes.attacks.attackC as Attacks
import src.classes.events.event_class_prototype as evt
import src.classes.entity.attribute as atr
import src.classes.temps.temp_class_handler as th
from src.classes.attacks.attackC import Instance



        


class Character:
    attacks: list[Attacks.Attack]


    def __init__(self, data_chara, _type : str):

        self._id = data_chara['_id']
        self.uuid = uuid.uuid4()

        self.name = data_chara['name']
        self.gender = data_chara['gender']
        self.age = data_chara['age']
        self.nick = data_chara['nick']
        self.desc = data_chara['desc']

        self.lines: dict[str,list] = data_chara['lines']

        self.alive = True

        self.ai : Ai = Ai("attack_all",self.uuid,_type)

        self.ids_attacks: list[int] = data_chara['attacks']

        self.attacks = abstraction.get_attack_class(self.ids_attacks)
        self.attack_slot: list[Instance] = []

        self.attributes: atr.Attributes | None  = atr.Attributes(data_chara,self)

        self.update_damage_attacks()

        self.abilities = []



        self.effects_handler: EffectHandler | None = EffectHandler(self)




        log(Log.DEBUG, f"[{self.name}]-->[{self.uuid}]", "[Character]")


    def check_abilities(self):
        for aby in self.abilities:
            if aby == "Phoenix Blessing" and aby not in self.attributes.temp_handler.flags:
                log(Log.DEBUG, f"{self.name} has the ability Phoenix Blessing")
                test = th.Temp("Fire","add",0,0,1000,True,False,False, "Phoenix Blessing")
                self.attributes.temp_handler.add_temp([test])

    def on_death_abylity(self):
        self.attributes.temp_handler.remove_temp(flags=self.abilities)

    
    def update_instances(self):
        active_list = []
        log(Log.DEBUG, "Updating Instances in attack slot", f"[{self.name}]")
        for instance in self.attack_slot:
            if instance.active:
                active_list.append(instance)
            self.attack_slot = active_list




    def add_id_attacks(self, ids: list[int] | list[str]):

        for ida in ids:
            if ida not in self.ids_attacks:
                self.ids_attacks.append(ida)
            else:
                print("Attack ID already exist")

        self.get_attacks()

    def remove_id_attacks(self,ids: list[int]):
        for ida in ids:
            if ida in self.ids_attacks:
                self.ids_attacks.remove(ida)

        self.get_attacks()



    def get_status(self,index: int):

            #Literal muito burro pra usar lambda
        if self.alive:
            alive = "Alive"
        else:
            alive = "Dead"

        if self.attributes is not None:
            print(f"[{index}][{self.ai.typeAi}][{self.name}][{alive}] Action: {self.attributes.actions} Level: {self.attributes.level} HP: {self.attributes.status.hp}/{self.attributes.status.maxHp} MP: {self.attributes.status.mp}/{self.attributes.status.maxMp} SPD: {self.attributes.status.spd}")
        else:
            print(f"[{index}][{self.ai.typeAi}][{self.name}][{alive}]")



    def get_info_attacks(self):
        attack : Attacks.Attack
        for attack in self.attacks:
            print(F"[A] {attack.name} | Target: {attack.target}/{attack.targetLimit} Intent: {attack.intent} Damages: {attack.get_total_dmg()}")


    def get_attacks(self):
        attack : Attacks.Attack
        print(self.ids_attacks)
        self.attacks = abstraction.get_attack_class(self.ids_attacks)
        self.update_damage_attacks()



    def update_damage_attacks(self):
        for attack in self.attacks:
            attack.set_damages(owner=self)



    def is_alive(self):
        if self.attributes.status.hp <= 0:
            self.alive = False
            self.attributes.status.hp = 0
            helpers.say_line(self,"incapacitated")
            print(f"{self.name} died.")
            return False
        else:
            return True
    

    def do_damage(self,dmg):
        if self.attributes.status.hp - dmg >= 0:
            self.attributes.status.hp -= dmg
        else:
            self.attributes.status.hp = 0
            self.is_alive()
     
    def on_damage(self,dmg_obj,damage_roll, owner):
        self.is_alive()

        if self.alive:
            
            damage_bonus = owner.attributes.elements[dmg_obj.main_element]
            res = self.attributes.resistances[dmg_obj.defType]
                    
            dmg_deal = (damage_roll + damage_bonus) * res 
            dmg_deal = trunc(dmg_deal)
            if dmg_deal <= 0:
                dmg_deal = 0

            old_hp = self.attributes.status.hp
            self.do_damage(dmg_deal)

            event = evt.On_Damage("on_damage",owner,self, dmg_obj=dmg_obj, damage=dmg_deal)

            types = f'|{self.name} taken {dmg_obj.name}({damage_roll}+{damage_bonus})*({res})| = {dmg_deal} damage | {self.name} HP:{old_hp}>{self.attributes.status.hp}.'
            return [types, event]
        else:
            return [f"{self.name} is dead.", None]
    

    def healing(self,damage_types : list):
        
        dmgType : damageTypes.DamageType
        
        if self.is_alive:
            
            for dmgType in damage_types:
                min_atk = dmgType.min_atk
                max_atk = dmgType.max_atk
                crit = self.attributes.status.crit
                max_crit = self.attributes.status.maxCrit
                dmg_bonus = self.attributes.elements[dmgType.main_element]

                min_roll = min_atk + crit
                max_roll = max_atk + max_crit

                if min_roll >= max_roll:
                    roll = min_roll
                else:
                    roll = random.randint(min_roll,max_roll)
        
                heal = roll + dmg_bonus

                if self.attributes.status.hp + heal < self.attributes.status.maxHp:
                    print(f"[{self.name}][HP:{self.attributes.status.hp}/{self.attributes.status.maxHp}] curou {heal} e ficou com {self.attributes.status.hp + heal} de vida")
                    self.attributes.status.hp += heal
                else:
                    print(f"[{self.name}][HP:{self.attributes.status.hp}/{self.attributes.status.maxHp}] curou {heal} e ficou com {self.attributes.status.hp} de vida")
        else:
            print("Já está morto, não tem como curar")

















