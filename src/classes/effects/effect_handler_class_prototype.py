from __future__ import annotations

from inspect import stack

from src.classes.effects.effect_class_prototype import Effect
import uuid

class EffectHandler:
    effects: list[Effect] = []
    effects_ids: list[uuid.UUID] = []
    typo_list: list[str] = []

    def update_effects_uuid(self):
        if len(self.effects) > 0:
            for effect in self.effects:
                if effect.uuid not in self.effects_ids:
                    self.effects_ids.append(effect.uuid)

    def remove_effects_uuid(self,uid: uuid.UUID):
        if uid in self.effects_ids:
            self.effects_ids.remove(uid)
            self.update_effects_uuid()

    def update_effect_typos(self):
        if len(self.effects) > 0:
            for effect in self.effects:
                if effect.typo not in self.typo_list:
                    self.typo_list.append(effect.typo)

    def remove_effects_typos(self, typo: str):
        if typo in self.typo_list:
            self.typo_list.remove(typo)
            self.update_effect_typos()

    def add_effects(self, effects: list[Effect]):
        self.update_effects_uuid()
        self.update_effect_typos()
        for effect in effects:
            if effect.uuid not in self.effects_ids and effect.typo not in self.typo_list:
                self.effects.append(effect)
                self.update_effects_uuid()
                self.update_effect_typos()
                print(f"[+] Effect {effect.name} added to Effects Handler")
            elif effect.typo in self.typo_list and effect.is_stackable:
                self.update_stack(effect.typo, effect)



    def update_stack(self, typo: str, eft: Effect):
        for effect in self.effects:
            if effect.typo == typo:
                print(f"[=] Stack adicionado em {effect.name}")
                effect.stacks += eft.stacks
                effect.turn += eft.turn



    def process_effects(self):
        for effect in self.effects:
            if effect.process_effect():
                print(f"[+] Effect {effect.name} processado")
            else:
                self.remove_effects(effect)

    def remove_effects(self,effect: Effect):
        self.effects.remove(effect)
        self.remove_effects_uuid(effect.uuid)




