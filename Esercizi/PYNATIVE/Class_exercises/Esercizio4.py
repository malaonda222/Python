# Ereditarietà delle classi

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return (f"The seating capacity of {self.capacity} is {capacity} passengers.")

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
    
scuola_bus = Bus("School Volvo", 180, 12)
print(scuola_bus.seating_capacity())
    