class User:
    def __init__(self, cognome:str, email:str, password:str):
        self.cognome = cognome
        self.email = email 
        self.password = password

    def __repr__(self):
        return f"{self.cognome}: {self.email} \n{self.password}"
    
    def register(self):
        print(f"Inserendo {self.cognome} con l'email {self.email} e la password {self.password}")


user = User("Giampiero", "giampiero@gmail.com", "giampiero99") #istanza
print(user)
user.register()
user.ban()
