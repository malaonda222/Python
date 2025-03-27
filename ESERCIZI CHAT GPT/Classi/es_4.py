class Car:
    total_cars = 0

    @classmethod
    def produce_cars(cls):
        cls.total_cars += 1
    
    @classmethod
    def get_total_cars(cls):
        return cls.total_cars
    
Car.produce_cars()
Car.produce_cars()

print(f"Il numero di auto prodotte è: {Car.get_total_cars()}")