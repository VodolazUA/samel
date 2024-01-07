# taks #3

from abc import ABC, abstractclassmethod


class Vehicle(ABC):
    
    def __init__(self, name: str, age: int, operable=True):
        self.name = name
        self._age = age
        self.__operable = operable
        
        print(f"New vehicle has been created: <{self.name}> (age: {self._age}), operable={self.__operable}")


    def get_operable_state(self):
        return self.__operable
    
    def __str__(self):
        return f"{self.name}"
    
    @abstractclassmethod
    def move(self) -> str:
        pass
        
    def stop(self):
        print(f"{self.name} has stopped.") 

    def is_older_than(self, car):
        return self._age > car._age
    
    @classmethod
    def get_unoperable(cls, vehicles):
        unoperable = [vehicle for vehicle in vehicles if vehicle.move() == ""]
        return unoperable


class Plane(Vehicle):

    def move(self):
        if self.get_operable_state():
            return "is flying."
        else:
            return ""
    

class Boat(Vehicle):

    def move(self):
        if self.get_operable_state():
            return "is sailing."
        else:
            return ""


class Car(Vehicle):
    
    @abstractclassmethod
    def move(self) -> str:
        pass

    def change_gear(self, new_gear):
        print(f"Current gear is {new_gear}.")

    def honk(self):
        print("Beep beep!!!")
      

class ElectricCar(Car):

    def _is_charged(self):
        return True
    
    def move(self) -> str:
        if (
            self._is_charged() and 
            self._is_engine_on() and 
            self._are_wheels_rotating()
        ):
            return "is driving (super mega eco green)."
        else:
            return ""
          

class GasCar(Car):

    def move(self) -> str:
        if self.get_operable_state():
            return "is driving."
        else:
            return ""
        
    def fill_up(self):
        print(f"{self.name} has been filled up.")


class Sled(Vehicle):
    
    def move(self) -> str:
        if self.get_operable_state():
            return "is sliding."
        else:
            return ""

if __name__ == "__main__":
    
    vehicles = []
    vehicles.append(Boat("Pirogoff", 47, False))
    vehicles.append(Plane("Boeing 777", 12, False))
    vehicles.append(ElectricCar("Tesla Model 3 Dual Motor", 2))
    vehicles.append(GasCar("Audi RS6", 1, True))
    vehicles.append(Sled("Santa's Lamba", 999))
    
    print("\n---------\n")

    for vehicle in vehicles:
        print(vehicle, vehicle.move())

    # відбір ТЗ які НЕ на ходу  
    unoperable = Vehicle.get_unoperable(vehicles)
    print("\nThere is a list of unoperable vehicles:")
    for uv in unoperable:
        print(" ->", uv)
        