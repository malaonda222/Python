class Giocatore:
    def __init__(self):
        self.nome = ""
        self.cognome = ""
        self.ruolo = ""

    def __str__(self):
        return f"Informazioni del giocatore: {self.nome} {self.cognome} - {self.ruolo}"
    
    def setName(self, nome:str):
        if not nome.isalpha():
            raise ValueError("Errore. Il nome deve essere composto solo da lettere.")
        else:
            self.nome = nome 

    def setLastname(self, cognome:str):
        if not cognome.isalpha():
            raise ValueError("Errore. Il nome deve essere composto solo da lettere.")
        else:
            self.cognome = cognome 

    def setRuolo(self, ruolo:str):
        if not ruolo.isalpha():
            raise ValueError("Errore. Il nome deve essere composto solo da lettere.")
        else:
            self.ruolo = ruolo 

    def getName(self) -> str:
        return self.nome

    def getLastname(self) -> str:
        return self.cognome

    def getRuolo(self) -> str:
        return self.ruolo 


class Squadra:
    def __init__(self):
        self.nome_squadra = ""
        self.giocatori = []
    
    def aggiungi_giocatore(self, giocatore:Giocatore):
        self.giocatori.append(giocatore)

    def setSquadra(self, nome_squadra:str):
        if not nome_squadra.isalpha():
            raise ValueError("Errore. Il nome deve essere composto solo da lettere.")
        else:
            self.nome_squadra = nome_squadra 

    def getSquadra(self) -> str:
        return self.nome_squadra
    
    def mostra_squadra(self):
        for item in self.giocatori:
            print(item.getName())
    
    def conta_giocatori(self):
        return len(self.giocatori)
    

calciatore1 = Giocatore()
calciatore1.setName("Mario")
calciatore1.setLastname("Rossi")
calciatore1.setRuolo("Attaccante")
print(calciatore1)

lion = Squadra()
lion.setSquadra("Lion")
# lion.aggiungi_giocatore("Rino", "Gaetano", 41)
lion.aggiungi_giocatore(calciatore1)
lion.mostra_squadra()
lion.conta_giocatori()