class hero():
    def __init__(self,name,role,dmg_type):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = 100
        self.auto_atk_dmg = 10
        
    def describe(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power"
        
hero_support1 = hero("estes","support", "healing support")
hero_mm1 = hero("lesley","marksman", "attack damage")
hero_fighter1 = hero("argus","fighter", "attack damage")
hero_tank1 = hero("atlas","tank", "defence")
hero_mage1 =  hero("lunox","mage", "magic attack")


print(f''' 
{hero_mm1.name}
{hero_mm1.role}
{hero_mm1.health} HP
{hero_mm1.auto_atk_dmg} Basic attack damage
{hero_mm1.dmg_type}
{hero_mm1.describe()}

{hero_fighter1.name}
{hero_fighter1.role}
{hero_fighter1.health} HP
{hero_fighter1.auto_atk_dmg} Basic attack damage
{hero_fighter1.dmg_type}
{hero_fighter1.describe()}

{hero_support1.name}
{hero_support1.role}
{hero_support1.health} HP
{hero_support1.auto_atk_dmg} Basic attack damage
{hero_support1.dmg_type}
{hero_support1.describe()}

{hero_tank1.name}
{hero_tank1.role}
{hero_tank1.health} HP
{hero_tank1.auto_atk_dmg} Basic attack damage
{hero_tank1.dmg_type}
{hero_tank1.describe()}

{hero_mage1.name}
{hero_mage1.role}
{hero_mage1.health} HP
{hero_mage1.auto_atk_dmg} Basic attack damage
{hero_mage1.dmg_type}
{hero_mage1.describe()}
''')