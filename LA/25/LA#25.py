print("LA#25")

from abc import ABC, abstractmethod
class Character(ABC):
    pass
    @abstractmethod
    def aliasOF(self):
        pass
class Batman(Character):
    def __init__(self, real_name, __alias):
        self.real_name = real_name
        self.alias = __alias
    @property
    def aliasOF(self):
        return f"His alias is {self.__alias} "
    
dknight = Batman("Bruce Wayne", "Batman")
print(dknight.alias)
