from abc import ABC, abstractmethod
"""this is the job class for characters. each character has one, if not
multiple jobs. each character can have any job it desires."""
class Job(ABC):

    @abstractmethod
    def getSkillModifier(self):
        """this will get the int value for the skill modifier of the selected job """
        pass

    @abstractmethod
    def combatMod(self):
        """this will return the int value for the combat mod for each job """
        pass

    @abstractmethod
    def levelBonuses(self):
        """this will return the double value of levelbonuses for each job"""
        pass