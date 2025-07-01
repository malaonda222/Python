class Ristorante:
    def __init__ (self, restaurant_name:str, cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Il ristorante si chiama \"{self.restaurant_name}\" e la cucina è {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("Il ristorante è aperto!")
    
if __name__ == "__main__":

    ristorante = Ristorante("Da i'Ganzo", "toscana")
    ristorante.describe_restaurant()
    ristorante.open_restaurant()