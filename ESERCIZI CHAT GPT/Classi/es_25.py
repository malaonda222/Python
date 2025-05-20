class Giocatore:
    def __init__(self, nickname: str):
        self.nickname = nickname 
    
    def __str__(self):
        return f"Nickname giocatore: {self.nickname}"

class Partita:
    def __init__(self, giocatore_bianco: str, giocatore_nero: str):
        self.giocatore_bianco = giocatore_bianco
        self.giocatore_nero = giocatore_nero 

    def __str__(self):
        return f"Giocatore bianco: {self.giocatore_bianco}; Giocatore nero: {self.giocatore_nero}"
    
class EsitoPunteggio:
    def __init__(self, punteggio_bianco: int, punteggio_nero:int):
        self.punteggio_bianco = punteggio_bianco
        self.punteggio_nero = punteggio_nero
    
    def vincitore(self):
        if self.punteggio_bianco > self.punteggio_nero:
            return f"Ha vinto il giocatore bianco." 
        elif self.punteggio_nero > self.punteggio_bianco:
            return f"Ha vinto il giocatore nero." 
        else:
            return None
    
giocatore = Giocatore("Titti")
print(giocatore)
giocatore1 = Giocatore("Riki")
partita = Partita("Titti", "Riki")
print(partita)
esito = EsitoPunteggio(89, 85)
print(esito.vincitore())
