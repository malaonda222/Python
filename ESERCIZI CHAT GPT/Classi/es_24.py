class Giocatore:
    def __init__(self, nickname:str, nome:str, cognome:str, indirizzo: str, rank:float):
        self.nickname = nickname 
        self.nome = nome 
        self.cognome = cognome
        self.indirizzo = indirizzo 
        self.rank = rank 
    
    def aggiorna_rank(self, nuovo_rank:str):
        self.rank = nuovo_rank
        print(f"Rank del giocatore {self.nickname} aggiornato a {self.rank}.")

    def confonta_rank(self, nuovo_giocatore:str):
        if self.rank > nuovo_giocatore.rank:
            print(f"Il giocatore uno {self.nickname} ha un rank maggiore di {nuovo_giocatore.nickname}.")
        elif nuovo_giocatore.rank > self.rank:
            print(f"Il giocatore due {nuovo_giocatore.nickname} ha un rank maggiore di {self.nickname}.")
        else:
            print(f"Il rank dei giocatori {nuovo_giocatore.nickname} e {self.nickname} è pari.")

    def stampa_info(self):
        print(f"Nickname: {self.nickname}\nNome: {self.nome}\nCognome: {self.cognome}\nIndirizzo: {self.indirizzo}\nRank: {self.rank}")

class Partita:
    def __init__(self, data:int, luogo:str, regole:str, komi: float, giocatore_bianco: str, giocatore_nero:str):
        self.data = data
        self.luogo = luogo 
        self.regole = regole 
        self.komi = komi 
        self.giocatore_bianco = giocatore_bianco 
        self.giocatore_nero = giocatore_nero 

    def stampa_riepilogo(self):
        print(f"La partita si svolge in data {self.data} e si svolge a {self.luogo}.\nLe regole sono le seguenti: {self.regole}.\nIl komi di ogni giocatore è: {self.komi}.\nIl giocatore bianco è {self.giocatore_bianco} e il giocatore nero è {self.giocatore_nero}.")

class Esito:
    def __init__(self):
        pass 

class EsitoRinuncia(Esito):
    def __init__(self, rinunciatario:str):
        self.rinunciatario = rinunciatario
    
    def descrizione(self):
        return f"La partita si è conclusa a causa della rinuncia del giocatore {self.rinunciatario}."
    
class EsitoPunteggio(Esito):
    def __init__(self, punteggio_bianco: float, punteggio_nero: float):
        self.punteggio_bianco = punteggio_bianco
        self.punteggio_nero = punteggio_nero
    
    def descrizione(self):
        if self.punteggio_bianco > self.punteggio_nero:
            vincitore = "Bianco"
        elif self.punteggio_bianco < self.punteggio_nero:
            vincitore = "Nero"
        else: 
            vincitore = "Pareggio"            
        return f"La partita è finita nel seguente modo: {vincitore} vince: {self.punteggio_bianco} - {self.punteggio_nero}"



giocatore = Giocatore("Rick19", "Riccardo", "Nipi", "Via Napoli 2", 3)
giocatore.stampa_info()
partita = Partita("20-04-2025", "Roma", "giapponesi", 6.5, "Nino99", "blackjack")
partita.stampa_riepilogo()
esito1 = EsitoRinuncia("Rick19")
print(esito1.descrizione())
esito2 = EsitoPunteggio(45, 22)
print(esito2.descrizione())
giocatore2 = Giocatore("Gigio17", "Giorgio", "Sassi", "Via Giotto 8", 8)
giocatore.aggiorna_rank(5)
giocatore.aggiorna_rank(15)
giocatore.stampa_info()
giocatore.confonta_rank(giocatore2)
