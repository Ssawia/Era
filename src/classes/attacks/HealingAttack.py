import src.classes.entitiesC as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.attacks.attackC as Attack

Attack = Attack.Attack

class HealingAttack(Attack):
    def __init__(self,_id,_class,name,desc,target,targetLimit,intent,damage,cost,hits,dmgType):
        super().__init__(_id=_id, _class=_class, name=name, desc=desc,target=target,targetLimit=targetLimit,intent=intent,damage=damage,cost=cost,hits=hits,dmgType=dmgType)
    

    def doDamage(self, owner : Chara.Character, queue: list, ai = False):
        if not ai:
            self.init_select(queue)
            queue = self.check_target(owner)

        obj : Chara.Character 

        for obj in queue:
            for c in range(self.hits):
                obj.healing(self.dmgList)

        return True  