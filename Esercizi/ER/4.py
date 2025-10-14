'''Crea una classe UserManager per gestire un sistema di utenti.
Ogni utente è rappresentato da:
uno username (stringa univoca),
un nome (stringa),
un email (stringa),
un flag attivo (booleano, True se l’utente è attivo)
{
    "marco89": {
        "nome": "Marco Bianchi",
        "email": "marco.bianchi@email.com",
        "attivo": True
    },
    ...
}

class UserManager:
    def __init__(self, utenti: dict[str, dict] = None):
    
- add_user(self, username: str, nome: str, email: str) -> dict | str
Aggiunge un nuovo utente con stato attivo = True.
Se l’username esiste già, solleva ValueError.

- deactivate_user(self, username: str) -> dict | str
Imposta attivo = False.
Se l’utente non esiste, solleva ValueError.

- reactivate_user(self, username: str) -> dict | str
Imposta attivo = True.
Se l’utente non esiste, solleva ValueError.

- remove_user(self, username: str) -> dict | str
Rimuove un utente dal sistema.
Se l’utente non esiste, solleva ValueError.

- update_user(self, username: str, nuovo_nome: str, nuova_email: str) -> dict | str
Aggiorna nome ed email dell’utente.
Se l’utente non esiste, solleva ValueError.

- get_user(self, username: str) -> dict | str
Restituisce i dati dell’utente.
Se non esiste, restituisce "Utente non trovato".

- list_users(self) -> list[str]
Restituisce la lista degli username.
'''

class UserManager:
    def __init__(self, utenti: dict[str, dict] = None) -> None:
        self.utenti = utenti if utenti is not None else {}

    def add_user(self, username: str, nome: str, email: str) -> dict|str:
        if username in self.utenti:
            raise ValueError("Errore. L'utente esiste già")
        else:
            self.utenti[username] = {"nome": nome, "email": email, "attivo": True}
            return {username: self.utenti[username]}
        
    def deactivate_user(self, username: str) -> dict|str:
        if username in self.utenti:
            raise ValueError("Errore. L'utente non esiste")
        else:
            self.utenti[username]["attivo"] = False 
            return {username: self.utenti[username]}
        
    def reactivate_user(self, username: str) -> dict|str:
        if username not in self.utenti:
            raise ValueError("Errore. L'utente non esiste")
        else:
            self.utenti[username["attivo"]] = True 
            return {username: self.utenti[username]}
        
    def remove_user(self, username: str) -> dict|str:
        if username not in self.utenti:
            raise ValueError("Errore. L'utente non esiste")
        else:
            rimosso = self.utenti.pop(username)
            return {username: rimosso}
        
    def update_user(self, username: str, nuovo_nome: str, nuova_email: str) -> dict|str:
        if username not in self.utenti:
            raise ValueError("Errore. L'utente non esiste")
        else:
            self.utenti[username]["nome"] = nuovo_nome
            self.utenti[username]["email"] = nuova_email
            return {username: self.utenti[username]}
        
    def get_user(self, username: str) -> dict|str:
        if username not in self.utenti:
            raise ValueError("Errore. Utente non trovato.")
        else:
            return {username: self.utenti[username]}
    
    def list_users(self)-> list[str]:
        if not self.utenti:
            raise ValueError("Errore. La lista utenti è vuota")
        else:
            return list(self.utenti.keys())
        
