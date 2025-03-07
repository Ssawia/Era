from __future__ import annotations
from src.classes.effects.effect_class import Effect
from helpers import log, Log
import uuid

class EffectHandler:

    def __init__(self, parent) -> None:
        self._parent = parent
        self.effects: list[Effect] = []
        self.effects_ids: list[uuid.UUID] = []
        self.typo_list: list[str] = []

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
                log(Log.DEBUG, f"Effect {effect.name} added to Effect Handler", f"[{self._parent.name}][EffectHandler]")
            elif effect.typo in self.typo_list and effect.is_stackable and effect.stacks <= effect.max_stacks:
                self.update_stack(effect.typo, effect)


    def update_stack(self, typo: str, eft: Effect):
        for effect in self.effects:
            if effect.typo == typo:
            
                effect.stacks += eft.main_stacks
                effect.turn += eft.main_turn
                log(Log.INFO, f" Stack add to {effect.name} at {effect.stacks}/{effect.max_stacks} to {effect.turn} turns.")



    def process_effects(self):
        if len(self.effects) > 0:
            for effect in self.effects:
                if effect.process_effect():
                    log(Log.DEBUG, f"Effect {effect.name} processado", f"[{self._parent.name}][EffectHandler]")
                else:
                    self.remove_effects(effect)
        else:
            log(Log.DEBUG, f"Has no effect to process", f"[{self._parent.name}][EffectHandler]")

    def remove_effects(self,effect: Effect):
        self.effects.remove(effect)
        self.remove_effects_uuid(effect.uuid)




