print("LA#22")

class Bday:
    def __init__(self, party_theme, list_of_foods):
        self.party_theme = party_theme
        self.list_of_foods = list_of_foods
    def foods(self):
        print("")
        print("Here is the list of foods Cake, pansit, puto")
        self.__secret_dish()
    def __secret_dish(self):
        print(f"Here is the list of secret foods{self.list_of_foods}")

anime = Bday("Shonen","Palabook, Graham")
marvel = Bday("Avengers","lumpia")
kupal = Bday("malupiton","Lechon")

anime.foods()
marvel.foods()
kupal.foods()
