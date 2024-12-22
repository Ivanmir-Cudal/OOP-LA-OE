print("LA#12")
class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price
       
    def describeToy(self):
        print(f"the toy {self.name} has a price of {self.price}")
   
class Car(Toy):
    def __init__(self, brand, model):
        super().__init__( brand, model)
       
ty = Car("Fire Truck", "60k")
ty.describeToy()
