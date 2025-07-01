class User:
    def __init__(self, first_name:str, last_name:str, age:int, genre:str, login_attempts:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.genre = genre
        self.login_attempts = login_attempts
    
    def describe_user(self):
        print(f"\nFirst name: {self.first_name}\nLast name: {self.last_name}\nAge: {self.age}\nGenre: {self.genre}\nLogin attempts: {self.login_attempts}")
    
    def greet_user(self):
        print(f"Ciao {self.first_name}, how you're doing?")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempt(self):
        self.login_attempts = 0
    

gino = User("Gino", "Rossi", 65, "maschio", 2)
gino.increment_login_attempts()
gino.increment_login_attempts()
gino.increment_login_attempts()
gino.increment_login_attempts()
gino.describe_user()

gino.reset_login_attempt()
gino.describe_user()