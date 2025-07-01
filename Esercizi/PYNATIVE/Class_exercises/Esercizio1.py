#  Create a Class with instance attributes

class Vehicle:
    def __init__(self, max_speed:int, mileage:int):
        self.max_speed = max_speed
        self.mileage = mileage 

    def __str__(self):
        return (f"La velocità massima è {self.max_speed} e il kilometraggio è di {self.mileage} km.")
    
    def __call__(self):
        if self.max_speed <= 30:
            return ("Velocità adatta a centri abitati.")
        elif 30 < self.max_speed <= 90:
            return ("Velocità adatta a strade provinciali e statali.")
        else:
            return ("Velocità adatta a autostrade.")


auto = Vehicle(50, 3000)
print(auto.max_speed, auto.mileage)
print(auto)

print(auto()) 