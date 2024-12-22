print("LA#11")
class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
       
    def describePhone(self):
        print(f"{self.brand} is {self.model}")
   
class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)
       
cp = Android("Xiomi", "note 12 pro")
cp.describePhone()
