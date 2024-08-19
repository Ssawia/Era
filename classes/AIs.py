from __future__ import annotations
import classes.entitiesC as ent
import classes.attacks.attackC as atk
from random import choice
from typing import List



class Ai:
     def __init__(self, behave, hostUuid,typeAi) -> None:
          self.typeAi = typeAi
          self.hostUuid = hostUuid
          self.behave = behave
     

     def set_behave(self, host : ent.Character):
          pass

     def decide_attack(self, host : ent.Character, queue ):
          if self.behave == "attack":
               attack: atk.Attack
               host_attack: atk.Attack
               target_attack: atk.Attack
               targets_attacks: List[atk.Attack] = []


               attacks = host.attacks

               for target_attack in attacks:
                    if target_attack.target != "self":
                         targets_attacks.append(target_attack)
               



               attack = choice(targets_attacks)
               print(f"{host.name} escolheu o ataque {attack.name}")

               uuid = attack.uuid
               idd = 0

               dmg_list: List[ent.Character] = []
               
               for host_attack in host.attacks:
                    if host_attack.uuid == uuid:
                         host.attacks[idd].init_select(queue)
                         host.attacks[idd].select.get_intent_on_queue()

                         target = host.attacks[idd].target
                         target_limit = host.attacks[idd].targetLimit
                         targets_list = host.attacks[idd].select.listt

                         if target == "select":
                              dmg_list = select_ai(target_limit,targets_list,host)
                         elif target == "single":
                              dmg_list = select_ai(target_limit,targets_list,host)
                         elif target == "multi":
                              print(f'{host.name} escolheu todos para atacar')
                              dmg_list = targets_list

                         host.attacks[idd].doDamage(host,dmg_list,True)

                    idd += 1


def select_ai(target_limit, targets_list: List[ent.Character],host: ent.Character):
     dmg_list: List[ent.Character] = []
     for c in range(target_limit):
          target_choice = choice(targets_list)
          print(f'{host.name} escolheu {target_choice.name} para atacar')
          dmg_list.append(target_choice)
          targets_list.remove(target_choice)
     
     return dmg_list

               






          



