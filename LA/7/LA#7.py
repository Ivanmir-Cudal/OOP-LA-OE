print("LA#7")

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color 
        
car1 = Car("Toyota", "Grey")
print(car1.brand,car1.color)

car1.color = "Red"
print(car1.brand,car1.color)

car2 = Car("Nissan", "Red")
print(car2.brand,car2.color)
