import classes.entitiesC as Chara
import classes.damages.damageTypeC as dmgType
import classes.attacks.attackC as Attack

Attack = Attack.Attack

class HealingAttack(Attack):
    def __init__(self,_id,_class,name,desc,target,targetLimit,intent,damage,cost,hits,dmgType):
        super().__init__(_id=_id, _class=_class, name=name, desc=desc,target=target,targetLimit=targetLimit,intent=intent,damage=damage,cost=cost,hits=hits,dmgType=dmgType)
    

    def doDamage(self, owner : Chara.Character, queue: list):
        self.init_select(queue)
        queue = self.check_target(owner)

        obj : Chara.Character 


        i : dmgType.DamageType 
        dmgList  = []

        for i in self.types:
            i.setAttack(owner)
            dmgList.append(i)


        for obj in queue:
            for c in range(self.hits):
                obj.healing(dmgList)

        return True  