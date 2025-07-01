class Studente:
    def __init__(self, name:str, lastname:str):
        self.name = name
        self.lastname = lastname
        self.voti = []

    def aggiungi_voti(self, voto:str):
        if 0 <= voto <= 10:
            self.voti.append(voto)
        else:
            print(f"Voto non valido. Inserire un voto compreso tra 0 e 10.")
    
    def calcola_media(self):
        if not self.voti:
            return 0
        somma = 0
        for voto in self.voti:
            somma += voto 
        return somma / len(self.voti)
    
    def giudizio_finale(self):
        media = self.calcola_media()
        if media >= 6:
            print(f"Lo studente è stato promosso.")
        else:
            print(f"Lo studente è stato bocciato.")


lisa = Studente("Lisa", "Bandinelli")
lisa.aggiungi_voti(4)
lisa.aggiungi_voti(8)
lisa.aggiungi_voti(8)
print(lisa.calcola_media())
lisa.giudizio_finale()