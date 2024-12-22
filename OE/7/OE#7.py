print("OE#7")

class TekkenCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    def introduce(self, func_name):
        def pin(*args, **kwargs):
            print("Introducing...")
            func_name(*args, **kwargs)
            print("This character is Amazing!")
        return pin

tekken = TekkenCharacter("Lee","Hitman Stance")

@tekken.introduce
def character_intro():
    print(f"I am {tekken.name} and I can use the {tekken.ability}")
character_intro()
