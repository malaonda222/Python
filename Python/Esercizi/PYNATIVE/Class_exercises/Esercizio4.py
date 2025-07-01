# Ereditarietà delle classi

class Vehicle:
    def __init__(self, name:str, max_speed:int, mileage:int):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return (f"The seating capacity of {self.name} is {capacity} passengers.")

class Bus(Vehicle):
    def seating_capacity(self, capacity:int=50):
        return super().seating_capacity(capacity)
    
scuola_bus = Bus("School Volvo", 180, 12)
print(scuola_bus.seating_capacity())

