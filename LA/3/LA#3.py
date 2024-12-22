print("LA#3")

class Character:
    def __init__(hero, name, role):
        hero.name = name
        hero.role = role

    def description(hero):
        print(f"{hero.name} is a {hero.role} hero")

char = Character("lyla", "Marksman")

Character.description(char)

