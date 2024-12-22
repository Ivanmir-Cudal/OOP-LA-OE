print("LA#19")

class Adobo:
    def __init__(self, meat, wet_seasoning, dry_seasoning):
        self.meat = meat
        self.__wet_seasoning = wet_seasoning
        self.dry_seasoning = dry_seasoning
    def __str__(self):
        return f"My adobo has {self.meat} for meat and {self.wet_seasoning}, and {self.dry_seasoning}"
    def may_wetba(self):
        return self__wet_seasoning
adobo1 = Adobo("Chimken", "water, toyo, suka","asin, magic sarap")
adobo2 = Adobo("baboy", "toyo, suka","asin, magic sarap")
adobo3 = Adobo("kangkong", "toy, suka","asin, magic sarap")

print(adobo1.__wet_seasoning)
print(adobo2)
print(adobo3)
