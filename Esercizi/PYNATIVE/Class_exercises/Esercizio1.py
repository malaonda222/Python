#  Create a Class with instance attributes

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage 

modello1 = Vehicle(70, 8000)
print(modello1.max_speed, modello1.mileage)