
class Vehicle:
    

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        print(f"New vehicle has been created: <{name}>")

    def __str__(self):
        return f"{self.name} (age:{self.__age})"

    def drive(self):
        print(f"{self.name} is moving.")
    
    @property
    def age(self):
        return self.__age
    
    def stop(self):
        print(f"{self.name} has stopped.") 

    def is_older_than(self, car):
        return self.age > car.age


class Car(Vehicle):

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
    
    def drive(self):
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
    
    print("-----------")

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

    print(
        f"{tesla} is older than {audi}: {tesla.is_older_than(audi)}"   
    )
    
    print("Audi's age is:", audi.age)  # .age - это функция, которая задекорирована под проперти
    # значение возраста хранится в car.__age
