from __future__ import annotations
import src.classes.entity.character as ent
import src.classes.attacks.attackC as atk
from src.classes.attacks.attackC import Instance
from random import choice
from helpers import Log,log





class Ai:
     def __init__(self, behave, hostUuid,typeAi) -> None:
          self.typeAi = typeAi
          self.hostUuid = hostUuid
          self.behave = behave
     

     def set_behave(self, host : ent.Character, behave : str):
          self.behave = behave



     def decide_typeAttack(self, behave ,host : ent.Character, attacks : list[atk.Attack]):
          target_attack: atk.Attack
          targets_attacks: list[atk.Attack] = []

          if behave == "attack_all":
               for target_attack in attacks:
                    if target_attack.target != "self":
                         targets_attacks.append(target_attack)

          elif behave == "support_all":
               for target_attack in attacks:
                    if target_attack.intent != "harm":
                         targets_attacks.append(target_attack)              
          

          return targets_attacks




          

     def decide_attack(self, host : ent.Character | None = None, queue: list[ent.Character] | None = None, on_enemy : bool | None = None, args: list = None):

          if args is not None:
               host = args[0]
               queue = args[1]
               on_enemy = args[2]

          attack: atk.Attack
          host_attack: atk.Attack

          #Decide os tipos de ataques que vai aparecer na lista de ataques disponiveis, baseado no comportamento do AI. 
          targets_attacks: list[atk.Attack] = []
          targets_attacks = self.decide_typeAttack(self.behave, host, host.attacks)

          attack = choice(targets_attacks)

          uuid = attack.uuid
          idd = 0

          dmg_list: list[ent.Character] = []

          attacks_damage_list = []
               
          for host_attack in host.attacks:
               if host_attack.uuid == uuid:
                    host.attacks[idd].init_select(queue)
                    host.attacks[idd].select.get_intent_on_queue(on_enemy=on_enemy)

                    target = host.attacks[idd].target
                    target_limit = host.attacks[idd].targetLimit
                    targets_list = host.attacks[idd].select.listt

                    if target == "select":
                         dmg_list = select_ai(target_limit,targets_list,host,attack.name)
                    elif target == "single":
                         dmg_list = select_ai(target_limit,targets_list,host,attack.name)
                    elif target == "multi":
                         dmg_list = targets_list
                    elif target == "self":
                         dmg_list.append(host)
                    
                    
                    host.attacks[idd].owner = host
                    host.attacks[idd].ai = True

                    if host.attacks[idd] not in host.attack_slot:
                         log(Log.DEBUG, f"{host.attacks[idd].name} does not exist in {host.name} attack slot, adding...", f"[{host.name}]")
                         host.attacks[idd].battle_queue.append(dmg_list)
                         instance = Instance(host.attacks[idd], dmg_list, True, host)
                         host.attack_slot.append(instance)
                         log(Log.DEBUG, f"{host.attacks[idd].name} add in attack slot, {host.attack_slot}", f"[{host.name}]")




                    #helpers.say_line(host,'attack')
                    

               idd += 1
          
          
     





def select_ai(target_limit, targets_list: list[ent.Character],host: ent.Character, attack_name):
     dmg_list: list[ent.Character] = []
     for c in range(target_limit):
          if len(targets_list) > 0:
               target_choice = choice(targets_list)

               dmg_list.append(target_choice)
               targets_list.remove(target_choice)

     
     return dmg_list

               






          



