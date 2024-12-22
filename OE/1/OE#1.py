print("OE#1")

class hero():
    def __init__(self,name,role,dmg_type):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        
    def __str__(self):
        return "this is object"

    def describe(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power"
        
hero_support1 = hero("estes","support", "healing support")
hero_mm1 = hero("lesley","marksman", "attack damage")
hero_fighter1 = hero("argus","fighter", "attack damage")
hero_tank1 = hero("atlas","tank", "defence")
hero_mage1 =  hero("lunox","mage", "magic attack")

print(hero_support1.describe())
print(hero_mm1.describe())
print(hero_fighter1.describe())
print(hero_tank1.describe())
print(hero_mage1.describe())

