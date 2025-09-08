class Film:
    def __init__(self, titolo: str, durata_minuti: int) -> None:
        self.titolo = titolo 
        self.durata_minuti = durata_minuti
    
    def __str__(self) -> str:
        return f"FIlm: {self.titolo} - Durata: {self.durata_minuti} min"
    
class Sala:
    def __init__(self, numero_id: int, film_programmazione: Film, posti_totali: int, posti_prenotati: int) -> None:
        self.numero_id = numero_id
        self.film_programmazione = film_programmazione
        self.posti_totali = posti_totali
        self.posti_prenotati = posti_prenotati

    def prenota_posti(self, num_posti: int) -> bool:
        disponibili = self.posti_totali - self.posti_prenotati 
        if disponibili >= num_posti:
           self.posti_prenotati += num_posti
           print(f"Prenotati {num_posti} posti; Posti totali rimanenti: {self.posti_totali - self.posti_prenotati}")
           return True
        else:
            print(f"Non ci sono posti disponibili. Solo {disponibili} posti disponibili!")
            return False
        
    def posti_disponibili(self) -> str:
        posti_disponibili = self.posti_totali- self.posti_prenotati
        if posti_disponibili == 0:
            print("Non ci sono posti disponibili")
        return f"I posti disponibili nella sala sono: {posti_disponibili}"
    
class Cinema:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.cinema = [] 
    
    def aggiungi_sala(self, sala: Sala) -> None:
        self.cinema.append(sala)
        print("Sala aggiunta al cinema")
    
    def prenota_film(self, titolo_film: str, num_posti: int) -> str:
        for sala in self.cinema:
            if sala.film_programmazione.titolo == titolo_film:
                if sala.prenota_posti(num_posti):
                    return f"Prenotati {num_posti} posti per il film '{titolo_film}' nella sala {sala.numero_id}."
                else:
                    return f"Non ci sono abbastanza posti disponibili per il film '{titolo_film}' nella sala {sala.numero_id}."
        return f"Film '{titolo_film}' non è stato trovato in nessuna sala."
    

film1 = Film("C'era una volta Hollywood", 120)
film2 = Film("Baby Girl", 130)
film3 = Film("Django", 165)

sala1 = Sala(123, film1, 100, 90)
sala2 = Sala(134, film2, 70, 65)
sala3 = Sala(1243, film3, 50, 2)

uci = Cinema("UCI Cinemas")
uci.aggiungi_sala(sala1)
uci.aggiungi_sala(sala2)
uci.aggiungi_sala(sala3)

print(uci.prenota_film("Django", 3))
print(uci.prenota_film("Baby Girl", 6))