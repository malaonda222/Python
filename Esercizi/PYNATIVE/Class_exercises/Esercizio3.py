# creare una classe figlia Bus che erediterà tutte le variabili e i metodi della classe Vehicle

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass 

scuola_bus = Bus("School Volvo", 180, 12)
print("Name:", scuola_bus.name, "Speed:", scuola_bus.max_speed, "Mileage:", scuola_bus.mileage)
