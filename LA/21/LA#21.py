print("LA#21")

class Adobo:
    def __init__(self, meat, wet_seasoning, dry_seasoning):
        self.meat = meat
        self.__wet_seasoning = wet_seasoning
        self.dry_seasoning = dry_seasoning
    def __str__(self):
        return f"My adobo has {self.meat} for meat and {self.wet_seasoning}, and {self.dry_seasoning}"
    def may_wetba(self, child):
        return self.__wet_seasoning
    def addCarrot(self, add):
        self.__wet_seasoning += add
adobo1 = Adobo("Chimken", 4, 3)

adobo1.addCarrot(5)


print(adobo1.may_wetba(True))
