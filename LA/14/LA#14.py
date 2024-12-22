print("LA#14")
class Spiderman:
    def __init__(self, name, Age):
        self.name = name
        self.Age = Age
    def describeSpiderman(self):
        print(f"The name of this spiderman is {self.name} and age is {self.age} years old")
class Tobey(Spiderman):
    def __init__(self, name, Age, movieTitle):
        super().__init__(name, Age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, Age, movieTitle):
        super().__init__(name, Age)
        self.movieTitle = movieTitle
       
class Tom(Spiderman):
    def __init__(self, name, Age, movieTitle):
        super().__init__(name, Age)
        self.movieTitle = movieTitle
       
spider1 = Tobey("Tobey Maguire" , 49, "Spiderman1")
spider2 = Andrew("Andrew Garfield" , 41, "Spiderman2")
spider3 = Tom("Tom Holland" , 28, "Spiderman walang home")

print(f"{spider1.name.upper()} {spider1.movieTitle}")
print(f"{spider2.name.upper()} {spider2.movieTitle}")
print(f"{spider3.name.upper()} {spider3.movieTitle}")
