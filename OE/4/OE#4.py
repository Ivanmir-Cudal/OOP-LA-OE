print("OE4")
class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def attack(self, target):
        target.health = target.health - self.power
        print(f"{self.name} deal damage to {target.name} remaining healt {target.health}")
    def special_move(self):
        pass
    def defend(self, attacker):
        reduced_damage = attacker.power
        self.health -= reduced_damage
        print(f"{self.name} defends against {attacker.name}! {self.name}'s remaining health after defense: {self.health}")
class Warrior(Character):
    def special_move(self):
        print(f"Warrior uses shield bash")
        self.power *=2
class Mage(Character):
    def special_move(self):
        print(f"Mage cast Fireball!")
        return 100
class Archer(Character):
    def special_move(self):
        print(f"Archer shoots a Piercing Arrow")
        return self.power
class Monster(Character):
    def special_move(self):
        print(f"Monster Roar and gains extra health!")
        self.health += 58
        print(f"{self.name}'s health after roar: {self.health}")
       
p1 = Warrior("asta", 1500, 200)
p2 = Mage("Noel", 1000, 150)
p3 = Archer("elf", 1000, 100)

p4 = Monster("akuma", 2000, 150)

p1.attack(p4)
p1.special_move()
p1.attack(p4)

p2.attack(p4)
damage = p2.special_move()
p4.health -= damage
print(f"{p4.name}'s remaining health after Fireball: {p4.health}")

p3.attack(p4)
p3_special_power = p3.special_move()
p4.health -= p3_special_power
print(f"{p4.name}'s remaining health after Piercing Arrow: {p4.health}")

p4.attack(p1)
p4.special_move()
p4.attack(p2)
p4.special_move()
p4.attack(p3)
p4.special_move()

while(True):
    if(p1.health < p4.health):
        p1.special_move()
        p1.attack(p4)
