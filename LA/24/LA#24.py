print("LA#24")

from abc import ABC, abstractmethod
class GameCharacter(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def attack(self):
        pass
class warrior(GameCharacter):
    def attack(self):
        print("Swings sword!")
class mage(GameCharacter):
    def attack(self):
        print("Casts a fireball!")
class archer(GameCharacter):
    def attack(self):
        print("Shoots an arrow!")
class healer(GameCharacter):
    def attack(self):
        print("Casts healing spell on ally!")

        
dbz = warrior("balmond")
dbz1 = mage("balmond")
dbz2 = archer("balmond")
dbz3 = archer("balmond")

dbz.attack()
dbz1.attack()
dbz2.attack()
dbz3.attack()
