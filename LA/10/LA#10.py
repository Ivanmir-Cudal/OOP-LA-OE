print("LA#10")
class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
       
    def describeVehicle(self):
        print(f"{self.brand} is {self.model} with the fuel type {self.fuel_type}")
   
class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass
       
car1 = Car("Toyota", "Corolla", "Gasoline")
car1.describeVehicle()

moto1 = Motorcycle("Honda", "Click", "Gasoline")
moto1.describeVehicle()
