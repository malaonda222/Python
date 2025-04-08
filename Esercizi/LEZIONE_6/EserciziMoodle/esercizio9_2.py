class Ristorante:
    def __init__ (self, restaurant_name:str, cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Il ristorante si chiama \"{self.restaurant_name}\" e la cucina è {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("Il ristorante è aperto!")

ristorante1 = "Python", "americana"
ristorante1.describe_restaurant()
ristorante2 = "Da Elena", "romana"
ristorante2.describe_restaurant()
ristorante3 = "New Mexico", "messicano"
ristorante3.describe_restaurant()