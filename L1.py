
class Vehicle:
    
    def __init__(self, name, age):
        self.name = name
        print(f"New vehicle has been created: <{name}>")

    def __str__(self):
        return f"{self.name}"

    def drive(self):
        print(f"{self.name} is moving.")
    
    def stop(self):
        print(f"{self.name} has stopped.") 

    def is_older_than(self, car):
        return self.age > car.age


class Car(Vehicle):

    def change_gear(self, new_gear):
        print(f"Current gear is {new_gear}.")

    def honk(self):
        print("Beep beep!!!")
      

class ElectricCar(Car):
        
    def drive(self):
        print(f"{self.name} is moving (eco).")


class GasCar(Car):
    
    def fill_up(self):
        print(f"{self.name} has been filled up.")


if __name__ == "__main__":

    audi = ElectricCar("Audi e-tron", 3)
    audi.drive()
    audi.change_gear("Drive mode")
    audi.stop()
    audi.change_gear("Reverse mode")
    audi.stop()
    audi.honk()

    tesla = ElectricCar("Tesla model Y", 1)
    tesla.drive()
    tesla.change_gear("Drive mode")
    tesla.stop()
    tesla.change_gear("Reverse mode")
    tesla.stop()
    tesla.honk()
