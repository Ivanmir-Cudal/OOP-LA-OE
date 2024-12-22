print("LA:17")
class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self, target):
        target.health = target.health - self.attack_power
        print(f"{self.name} attacks {target.name}")
        print(f"{self.name} deals {self.attack_power} to {target.name} ")
        print(f"{target.name} has remaining {target.health} health")
    def heal(self, amount):
        amount.health = amount.health + self.health
        print(f"{amount.name} has restored his/her health {amount.health}")
player1 = Player("ivan pogi", 2000, 200)
player2 = Player("kupal", 1000, 150)

player1.attack(player2)
while(True):
    if(player1.health <= 0):
       print("player 2 wins")
       break
    elif(player2.health <= 0):
       print("player 1 wins")
       break
    else:
       player1.attack(player2)
player1.heal(player2)
"""print(player1.name, player1.health, player1.attack_power)
print(player2.name, player2.health, player2.attack_power)"""
