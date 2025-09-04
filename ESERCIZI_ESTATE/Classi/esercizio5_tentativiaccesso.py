'''Aggiungi un attributo chiamato tentativi_accesso alla tua classe Lettore, con valore 
iniziale 0.
Crea un metodo incrementa_tentativi_accesso() che aumenti il valore di 1 ogni volta che 
viene chiamato.
Crea un altro metodo azzera_tentativi_accesso() che reimposti il valore a 0.
Crea un’istanza della classe, chiama il metodo di incremento alcune volte, e stampa il 
valore.
Poi chiama il metodo di azzeramento e stampa di nuovo per verificare.'''

class Lettore:
    def __init__(self, nome: str, cognome: str, genere_preferito: str, eta: int, iscritto: bool, tentativi_accesso = 0) -> None:
        self.nome = nome
        self.cognome = cognome 
        self.genere_preferito = genere_preferito
        self.eta = eta
        self.iscritto = iscritto 
        self.tentativi_accesso = tentativi_accesso

    def descrivi_lettore(self) -> str:
        print(f"Nome: {self.nome}\nCognome: {self.cognome}\nGenere preferito: {self.genere_preferito}\nEtà: {self.eta}\nIscritto: {self.iscritto}\nTentativi accesso: {self.tentativi_accesso}")

    def incrementa_tentativi_accesso(self) -> str:
        self.tentativi_accesso += 1
        print(f"Tentativi di accesso: {self.tentativi_accesso}")

    def azzera_tentativi_accesso(self) -> str:
        self.tentativi_accesso = 0
        print(f"Tentativi azzerati")

lettore = Lettore("Gianluca", "Errico", "Fantasy", 28, True, 3)
lettore.descrivi_lettore()
lettore.incrementa_tentativi_accesso()
lettore.azzera_tentativi_accesso()