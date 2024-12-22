print("LA#4")

class Character:
    def __init__(hero, name, role):
        hero.name = name
        hero.role = role

    def __str__(hero):
        return f"{hero.name} is a {hero.role} hero"


char = Character("lyla", "Marksman")

print(char)
