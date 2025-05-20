class Giocatore:
    def __init__(self, nome:str, ruolo:str, punteggio:int):
        self.nome = nome
        self.ruolo = ruolo 
        self.punteggio = punteggio 
    
    def __str__(self):
        return f"Nome: {self.nome}, Ruolo: {self.ruolo}, Punteggio: {self.punteggio}"
    
class Squadra:
    def __init__(self, nome):
        self.nome = nome
        self.giocatori = [] 
    
    def aggiungi_giocatore(self, giocatore:str):
        self.giocatori.append(giocatore)
        return f"Aggiunti {giocatore.nome} alla squadra {giocatore.ruolo}."
    
    def media_punteggi(self):
        if not self.giocatori:
            return 0 
        somma = 0
        for g in self.giocatori:
            somma += g.punteggio
        return f"La media dei punteggi dei giocatori è: {somma / len(self.giocatori)}."
    
    def miglior_giocatore(self):
        if not self.giocatori:
            return None 
        migliore = self.giocatori[0]
        for g in self.giocatori[1:]:
            if g.punteggio > migliore.punteggio:
                migliore = g 
        return f"Il miglior giocatore è: {migliore}."
    
g1 = Giocatore("Rino", "Attaccante", 10)
g2 = Giocatore("Renato", "Difensore", 7)
g3 = Giocatore("Tommaso", "Portiere", 4)

squadra = Squadra("San Giusto")
squadra.aggiungi_giocatore(g1)
squadra.aggiungi_giocatore(g2)
squadra.aggiungi_giocatore(g3) 

print(squadra.media_punteggi())
print(squadra.miglior_giocatore())
