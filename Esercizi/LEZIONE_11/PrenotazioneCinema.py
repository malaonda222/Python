class Film:
    def __init__(self, titolo: str, durata_minuti: int):
        self.titolo = titolo 
        self.durata_minuti = durata_minuti

    def __str__(self):
        return f"Il film si chiama {self.titolo} e la durata è di {self.durata_minuti} minuti."


class Sala: 
    def __init__(self, numero_id: int, film_in_prog: str, posti_totali: int):
        self.numero_id = numero_id
        self.film_in_prog = film_in_prog
        self.posti_totali = posti_totali
        self.posti_prenotati = 0

    def __str__(self):
        return f"La sala ha il seguente codice id: {self.numero_id}.\nIl film in programma è: {self.film_in_prog}\nAl momento in posti totali nella sala sono: {self.posti_totali}."
    
    def prenota_posti(self, num_posti: int):
        self.num_posti = num_posti
        if num_posti <= 0:
            print("Numero di posti non valido.")
        elif self.posti_prenotati + num_posti <= self.posti_totali:
            self.posti_prenotati += num_posti
            print("Prenotazione avvenuta con successo.")
        else:
            print(f"Errore. Ci sono solo {self.posti_totali} disponibili nella sala {self.numero_id}.")

    def posti_disponibili(self):
        print(f"I posti disponibili nella sala {self.numero_id} sono: {self.posti_totali - self.posti_prenotati}.")


class Cinema:
    def __init__(self):
        self.sale = []

    def aggiungi_sala(self, sala:Sala):
        if sala in self.sale:
            return "La sala è già presente nella lista."
        else: 
            self.sale.append(sala)
            return "Lista delle sale aggiornata."
        
    def prenota_film(self, titolo_film: str, num_posti: int):
        for sala in self.sale:
            if sala.film == titolo_film:
                return sala.prenota_posti(num_posti)
            else:
                return f"Film {titolo_film} non è stato trovato in nessuna sala."


film1 = Film("Changeling", 240)
print(film1)
sala1 = Sala(125, "Parasite", 2)
print(sala1)

sala1.prenota_posti(2)
sala1.posti_disponibili()


film2 = Film("Furia", 220)
print(film2)
sala2 = Sala(33, "Kill Bill", 8)
print(sala2)
sala2.prenota_posti(3)
sala2.posti_disponibili()

cinema = Cinema()
print(cinema.aggiungi_sala(sala1))
print(cinema.aggiungi_sala(sala2))

    

    
