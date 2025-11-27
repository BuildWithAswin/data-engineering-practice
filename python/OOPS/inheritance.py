class Animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name
    
    def sound(self):
        print(f"Every {self.type} makes a sound")

    
class Dog(Animal):
    def __init__(self,type, name):
        super().__init__(type, name)
    
    def sound(self):
        print(f"Every {self.type} does bow bow!. So does {self.name}!")

class Cat(Animal):
    def __init(self, type, name):
        super().__init__(type, name)
    
    def sound(self):
        print(f"Every {self.type} does meow meow!. So does {self.name}!")


  
dog1 = Dog("Dog", "Tommy")
dog1.sound()
        
cat1 = Cat("Cat", "Persia")   
cat1.sound()