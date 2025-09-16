'''1. Classe Utente
Attributi: nome, cognome, username, email
Metodi: descrivi_utente() e saluta_utente()

2. Classe Privilegi
Attributo: una lista di privilegi (es. "può aggiungere libri", "può rimuovere utenti")
Metodo: mostra_privilegi()

3. Classe Admin
Attributi: una istanza di Utente e una istanza di Privilegi
Il metodo mostra_privilegi_admin() deve semplicemente richiamare mostra_privilegi() sull’attributo privilegi'''

class Utente: 
    def __init__(self, nome: str, cognome: str, username: str, email: str) -> None:
        self.setNome(nome)
        self.setCognome(cognome)
        self.setUsername(username)
        self.setEmail(email)
    
    def setNome(self, nome: str) -> None:
        self._nome = nome 

    def setCognome(self, cognome: str) -> None:
        self._cognome = cognome 

    def setUsername(self, username: str) -> None:
        self._username = username 
    
    def setEmail(self, email: str) -> None:
        self._email = email 
    
    def nome(self) -> str:
        return self._nome 
    
    def cognome(self) -> str:
        return self._cognome 
    
    def username(self) -> str:
        return self._username 
    
    def email(self) -> str:
        return self._email 
    
    def descrivi_utente(self) -> str:
        print(f"Nome: {self.nome()}\nCognome: {self.cognome()}\nUsername: {self.username()}\nEmail: {self.email()}")

    def saluta_utente(self) -> str:
        print(f"Ciao, {self.nome()}!")

class Privilegi:
    def __init__(self, privilegi: list[str]) -> None:
        self.privilegi = privilegi 
    
    def mostra_privilegi(self) -> None:
        print("Privilegi dell'amministratore:")
        for privilegio in self.privilegi:
            print(f"- {privilegio}") 
    
class Admin:
    def __init__(self, utente: Utente, privilegio: Privilegi):
        self.utente = utente 
        self.privilegio = privilegio

    def mostra_privilegi_admin(self):
        self.privilegio.mostra_privilegi()


utente = Utente("Luisa", "Bianchi", "lubi", "luisa@gmail.com")

privilegi = Privilegi(["può aggiungere un libro", "può eliminare un libro dalla libreria", "può rimuovere utenti"])

admin = Admin(utente, privilegi)

utente.descrivi_utente()
utente.saluta_utente()
admin.mostra_privilegi_admin()