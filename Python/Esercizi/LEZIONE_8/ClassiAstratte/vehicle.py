from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod 
    def description(self) -> str:
        pass

class Car(Vehicle):
    def description(self) -> str:
        return "I am a car."
    
    def show_description(car) -> None:
        print(car.description())

class Bicycle(Vehicle):
    def description(self) -> str:
        return "I am a bicycle."
    
def show_description(vehicle: Vehicle) -> None:
    print(vehicle.description())


show_description(Car()) 
show_description(Bicycle())