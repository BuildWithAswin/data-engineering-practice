class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False # new attribute to check the car state
        
    def display_info(self):
        print(f"Car brand: {self.brand}")
        print(f"Car model: {self.model}")
    
    #adding methods , start and stop
    def drive(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} is running now!")
        else:
            print(f"{self.brand} {self.model} is already running!")

    def stop(self):
        if not self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} is stopped!")
        else:
            print(f"{self.brand} {self.model} is already stopped")

#objects created using car class
car1 = Car("Toyota", "Corolla")     
car2 = Car("Hyundai", "Santa Fe")

#methods of car class
car1.drive()
car2.stop()


    
    