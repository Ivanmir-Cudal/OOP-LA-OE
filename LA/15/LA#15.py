print("LA#15")
class Dog:
    def __init__(self, name):
        self.name = name
   
    def speak(self):
        print("Bark!")

class Cat:
    def __init__(self, name):
        self.name = name
   
    def speak(self):
        print("Meow!")

class Bird:
    def __init__(self, name):
        self.name = name
   
    def speak(self):
        print("Chirp!")
       
class Fish:
    def __init__(self, name):
        self.name = name
   
    def speak(self):
        print("...")  
       
dog = Dog("blackie")
cat = Cat("Ming-Ming")
bird = Bird("Birdie")
fish = Fish("Fishie")

def animal_sounds(animal):
    animal.speak()

animal_sounds(dog)
animal_sounds(cat)
animal_sounds(bird)

for x in [dog, cat, bird, fish]:
    x.speak()
