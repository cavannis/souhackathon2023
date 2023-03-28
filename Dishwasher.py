from DndInterface import Job

class Dishwasher(Job):

    def getSkillModifier(self):
        """dishwasher skillmodifier return function. 
        The dishwasher job gives a +5 to all pans"""
        PanModifier = 5
        

        return PanModifier
    def combatMod(self):
        """dishwasher combat mod return function.
        Returns a +1 to melee attacks """
        MeleeBonus = 1

        return MeleeBonus

    def levelBonuses(self):
        self = self + 1
        """dishwasher level bonus return function.
        each level increases the level of self by one"""

        return self