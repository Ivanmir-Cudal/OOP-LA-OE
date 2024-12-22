print("LA#13")
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
       
   
class child(Animal):
    def __init__(self, name, type, can_swim):
        super().__init__( name, type)
        self.can_swim = can_swim
       
ch = child("maru", "child",True)
print(ch.can_swim)
