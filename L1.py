# taks #3

class Vehicle:
    
    def __init__(self, name: str, age: int, operable=True):
        self.name = name
        self.move_statement = "is moving."
        self._age = age
        self.__operable = operable
        
        print(f"New vehicle has been created: <{self.name}> (age: {self._age}), operable={self.__operable}")

    def __str__(self):
        return f"{self.name}"

    def move(self):
        
        if self.__operable:
            return self.move_statement
        else:
            return ""
        
    def stop(self):
        print(f"{self.name} has stopped.") 

    def is_older_than(self, car):
        return self._age > car._age
    
    def get_unoperable(vehicles):
        unoperable = []
        for v in vehicles:
            if v.move() == "":
                unoperable.append(v)
        return unoperable


class Plane(Vehicle):
    
    def __init__(self, name: str, age: int, operable=True):
        super().__init__(name, age, operable)
        self.move_statement = "is flying."
    

class Boat(Vehicle):
    
    def __init__(self, name: str, age: int, operable=True):
        super().__init__(name, age, operable)
        self.move_statement = "is sailing."


class Car(Vehicle):

    def __init__(self, name: str, age: int, operable=True):
        super().__init__(name, age, operable)
        self.move_statement = "is driving."

    def _is_engine_on(self):
        return True
    
    def _are_wheels_rotating(self):
        return True
    
    def change_gear(self, new_gear):
        print(f"Current gear is {new_gear}.")

    def honk(self):
        print("Beep beep!!!")
      

class ElectricCar(Car):
    
    def __init__(self, name: str, age: int, operable=True):
        super().__init__(name, age, operable)
        # self.move_statement = f"{self.name} is driving (eco)."
    
    def _is_charged(self):
        return True
    
    def move(self):
        if (
            self._is_charged() and 
            self._is_engine_on() and 
            self._are_wheels_rotating()
        ):
            return "is driving (super mega eco green)."
        else:
            return ""


class GasCar(Car):
    
    def fill_up(self):
        print(f"{self.name} has been filled up.")


if __name__ == "__main__":
    
    vehicles = []
    vehicles.append(Boat("Pirogoff", 47))
    vehicles.append(Plane("Boeing 777", 12, False))
    vehicles.append(ElectricCar("Tesla Model 3 Dual Motor", 2))
    vehicles.append(GasCar("Audi RS6", 1))
    
    print("\n---------\n")

    for vehicle in vehicles:
        print(vehicle, vehicle.move())

    # відбір ТЗ які НЕ на ходу  
    unoperable = Vehicle.get_unoperable(vehicles)
    print("\nThere is a list of unoperable vehicles:")
    for uv in unoperable:
        print("-", uv)
        