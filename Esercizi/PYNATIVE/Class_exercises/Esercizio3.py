# creare una classe figlia Bus che erediterà tutte le variabili e i metodi della classe Vehicle

class Vehicle:
    def __init__(self, name:str, max_speed:float, mileage:float):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

scuolabus = Bus("Volvo", 80, 8000)
print(f"Le informazioni riguardo allo scuolabus sono le seguenti: nome: {scuolabus.name}, velocità: {scuolabus.max_speed}, kilometraggio: {scuolabus.mileage}.")