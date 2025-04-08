class Ristorante:
    def __init__ (self, restaurant_name:str, cuisine_type:str, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"Il ristorante si chiama \"{self.restaurant_name}\" e la cucina è {self.cuisine_type}. Il ristorante ha servito {self.number_served} tavoli.")
    
    def open_restaurant(self):
        print("Il ristorante è aperto!")

    def set_number_served(self, number_served:int) -> None:
        self.number_served = number_served        

    def increment_number_served(self, number_served:int) -> None:
        self.number_served += number_served


restaurant = Ristorante("Da Peppe", "romana", number_served = 10)
restaurant.describe_restaurant()
restaurant.set_number_served(9)
restaurant.describe_restaurant()
restaurant.increment_number_served(10)
restaurant.describe_restaurant()

