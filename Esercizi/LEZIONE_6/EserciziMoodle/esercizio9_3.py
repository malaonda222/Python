class User:
    def __init__(self, first_name:str, last_name:str, age:int, genre:str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.genre = genre
    
    def describe_user(self):
        print(f"\nFirst name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age}\nGenre: {self.genre}")
    
    def greet_user(self):
        print(f"Ciao {self.first_name}, how you're doing?")
    

Riccardo = User("Riccardo", "Boni", 26, "male")
Riccardo.describe_user()
Riccardo.greet_user()

Silvia = User("Silvia", "Rosi", 46, "female")
Silvia.describe_user()
Silvia.greet_user()