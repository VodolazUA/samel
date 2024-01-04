# taks #3

class Vehicle:
    
    def __init__(self, name, age):
        self.name = name
        self._age = age
        print(f"New vehicle has been created: <{name}> (age: {self._age})")

    def __str__(self):
        return f"{self.name} (age: {self._age})"

    def move(self):
        print(f"{self.name} is moving.")
    
    def stop(self):
        print(f"{self.name} has stopped.") 

    def is_older_than(self, car):
        return self._age > car._age


class Plane(Vehicle):
    
    def move(self):
        print(f"{self.name} is flying.")
    

class Boat(Vehicle):
    
    def move(self):
        print(f"{self.name} is sailing.")


class Car(Vehicle):

    def move(self):
        print(f"{self.name} is driving.")

    def _is_engine_on(self):
        return True
    
    def _are_wheels_rotating(self):
        return True
    
    def change_gear(self, new_gear):
        print(f"Current gear is {new_gear}.")

    def honk(self):
        print("Beep beep!!!")
      

class ElectricCar(Car):
    
    def _is_charged(self):
        return True
    
    def move(self):
        if (
            self._is_charged() and 
            self._is_engine_on() and 
            self._are_wheels_rotating()
        ):
            print(f"{self.name} is moving (eco).")
        else:
            print('Oh nooooo')


class GasCar(Car):
    
    def fill_up(self):
        print(f"{self.name} has been filled up.")


if __name__ == "__main__":
    
    vehicles = []
    vehicles.append(Boat("Pirogoff", 47))
    vehicles.append(Plane("Boeing 777", 12))
    vehicles.append(ElectricCar("Tesla Model 3 Dual Motor", 2))
    vehicles.append(GasCar("Audi RS6", 1))
    
    for v in vehicles:
        v.move()