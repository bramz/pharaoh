from abc import ABC
from abc import abstractmethod

class Skill(ABC):
    def __init__(self, stype: str):
        self.skill: str
        self.stype = stype

    @abstractmethod
    def add_skill(self, skill: str):
        pass
    
    @abstractmethod
    def remove_skill(self, skill: str):
        pass

    @abstractmethod
    def get_skill(self, stype: str):
        pass


class Carpentry(Skill):
    def __init__(self, stype: str):
        self.skill: str
        self.stype = stype

    def add_skill(self, skill: str):
        self.skill[self.stype] = skill

    def remove_skill(self, skill: str):
        if skill in self.skill[self.stype]:
            self.skill[self.stype] = None

    def get_skill(self):
        return self.skill[self.stype]
