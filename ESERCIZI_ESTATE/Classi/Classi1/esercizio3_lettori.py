'''Crea una classe chiamata Lettore.
Il metodo __init__() deve memorizzare nome, cognome e almeno altri due attributi che 
potrebbero appartenere a un profilo di lettore (es. genere_preferito, eta, 
iscritto_newsletter, ecc.).
Crea un metodo descrivi_lettore() che stampi un riepilogo delle informazioni del lettore.
Crea un metodo saluta_lettore() che stampi un saluto personalizzato.
Crea almeno due istanze della classe Lettore e chiama entrambi i metodi per ciascuna.'''

class Lettore:
    def __init__(self, nome: str, cognome: str, genere_preferito: str, eta: int, iscritto: bool) -> None:
        self.nome = nome
        self.cognome = cognome 
        self.genere_preferito = genere_preferito
        self.eta = eta
        self.iscritto = iscritto 

    def descrivi_lettore(self) -> str:
        print(f"Nome: {self.nome}\nCognome: {self.cognome}\nGenere preferito: {self.genere_preferito}\nEtà: {self.eta}\nIscritto: {self.iscritto}")
    
    def saluta_lettore(self):
        print(f"Benvenuto, {self.nome}")
    

lettore1 = Lettore("Fabio", "Ferri", "Narrativa", 33, True)
lettore2 = Lettore("Lucia", "Violanti", "Horror", 38, False)
lettore1.descrivi_lettore()
lettore2.descrivi_lettore()
lettore1.saluta_lettore()
lettore2.saluta_lettore()
