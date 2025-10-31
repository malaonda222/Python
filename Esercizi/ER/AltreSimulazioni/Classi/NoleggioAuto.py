class Car:
    def __init__(self, car_id: str, model: str, daily_rate: float) -> None:
        self.car_id: str = car_id
        self.model: str = model 
        self.daily_rate: float = daily_rate
        self.is_rented: bool = False 
    
    def rent(self) -> None:
        if not self.is_rented:
            self.is_rented = True 
        else:
            print(f"L'auto '{self.model}' è già noleggiata.")
    
    def return_car(self) -> None:
        if self.is_rented:
            self.is_rented = False 
        else:
            print(f"L'auto '{self.model}' non risulta attualmente noleggiata.")
    

class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id: str = customer_id
        self.name: str = name 
        self.active_rentals: list[Car] = []

    def rent_car(self, car: Car) -> None:
        if not car.is_rented:
            self.active_rentals.append(car)
            car.rent()
        else:
            print(f"L'auto '{car.model}' non è disponibile per il noleggio.")
    
    def return_car(self, car: Car) -> None:
        if car in self.active_rentals:
            self.active_rentals.remove(car)
            car.return_car()
        else:
            print(f"L'auto '{car.model}' non risulta tra i noleggi attivi del cliente.")
    

class CarRentalSystem:
    def __init__(self) -> None:
        self.cars: dict[str, Car] = {}
        self.customers: dict[str, Customer] = {}
    
    def add_car(self, car_id: str, model: str, daily_rate: float) -> None:
        if car_id in self.cars:
            print(f"Errore: auto con ID '{car_id}' già presente.")
        else:
            self.cars[car_id] = Car(car_id, model, daily_rate)
    
    def register_customer(self, customer_id: str, name: str) -> None:
        if customer_id in self.customers:
            print(f"Errore: cliente con ID '{customer_id}' già registrato.")
        else:
            self.customers[customer_id] = Customer(customer_id, name)
    
    def rent_car(self, customer_id: str, car_id: str) -> None:
        if customer_id in self.customers and car_id in self.cars:
            customer = self.customers[customer_id]
            car = self.cars[car_id]
            customer.rent_car(car)
        else:
            print("Cliente o auto non trovata.")
    
    def return_car(self, customer_id: str, car_id: str) -> None:
        if customer_id in self.customers and car_id in self.cars:
            customer = self.customers[customer_id]
            car = self.cars[car_id]
            customer.return_car(car)
        else:
            print("Cliente o auto non trovata.")
    
    def list_available_cars(self) -> list[str]:
        return [car_id for car_id, car in self.cars.items() if not car.is_rented]
    
    def list_customer_rentals(self, customer_id: str) -> list[str]|str:
        if customer_id not in self.customers:
            return "Errore: cliente non trovato."
        else:
            customer = self.customers[customer_id]
            return [car.car_id for car in customer.active_rentals]
    
rental = CarRentalSystem()

rental.add_car("c001", "Tesla Model 3", 99.99)
rental.add_car("c002", "Fiat 500", 39.99)

rental.register_customer("u001", "Luca Rossi")

rental.rent_car("u001", "c001")
print(rental.list_available_cars())

rental.return_car("u001", "c001")
print(rental.list_available_cars())
