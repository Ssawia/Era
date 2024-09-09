import src.classes.entitiesC as Chara
import src.classes.damages.damageTypeC as dmgType
import src.classes.attacks.attackC as Attack
from helpers import isCrit

Attack = Attack.Attack


class PhysicalAttack(Attack):
    def __init__(self,_id,_class,name,desc,target,targetLimit,intent,damage,cost,hits,dmgType):
        super().__init__(_id=_id, _class=_class, name=name, desc=desc,target=target,targetLimit=targetLimit,intent=intent,damage=damage,cost=cost,hits=hits,dmgType=dmgType)
    
    def doDamage(self, owner : Chara.Character, queue: list, ai = False):

        if not ai:
            self.init_select(queue)
            queue = self.check_target(owner)

        crit = isCrit(owner.attributes.status.crit)

        
        obj : Chara.Character

        

        for obj in queue:
            for c in range(self.hits):
                obj.defend(self.name,self.dmgList, owner, obj, crit)

        return True