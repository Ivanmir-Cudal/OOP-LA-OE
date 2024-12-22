print("LA#23")

class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    def introduce(self, func_name):
        def pin(*args, **kwargs):
            print("Introducing")
            func_name(*args, **kwargs)
            print("This character is Amazing!")
        return pin

Bleach = AnimeCharacter("Ichigo","Getsuga")

@Bleach.introduce
def character_info():
    print(f"I am {Bleach.name} and I can use the {Bleach.ability}")
character_info()
