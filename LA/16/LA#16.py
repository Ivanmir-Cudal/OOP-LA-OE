print("LA#16")
class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
       
    def operate(self):
        print("Operating")
       
    def info(self):
        print(f"the brand is {self.brand} model is {self.model}")
class WashingMachine(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Washing clothes!")
class Refrigerator(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Keeping food cold!")
class Microwave(Appliance):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def operate(self):
        print("Heating food!")

lg = WashingMachine("LG", "T2108NT1G")
samsung = Refrigerator("samsung", "SBFamily Hub™ Gentle Black Matt")
toshiba = Microwave("Toshiba", "EM131A5C-BS")

for appl in [lg, samsung, toshiba]:
    appl.operate()
lg.info()
samsung.info()
toshiba.info()
