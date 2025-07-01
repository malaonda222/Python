from abc import ABC, abstractmethod 

class Volo(ABC):
    def __init__(self, codice: str, capacita: int):
        self.codice = codice
        self.capacita = capacita
        self.prenotazioni = 0
    
    @abstractmethod
    def prenota_posto(self):
        pass
 
    @abstractmethod
    def posti_disponibili(self):
        pass
 
class VoloCommerciale(Volo):
    def __init__(self, codice: str, capacita: int):
        super().__init__(codice, capacita)
 
        self.posti_economica = int(capacita * 0.7)
        self.posti_business = int(capacita * 0.2)
        self.posti_prima = capacita - self.posti_economica - self.posti_business
 
        self.prenotazioni_economica = 0
        self.prenotazioni_business = 0
        self.prenotazioni_prima = 0

    def posti_disponibili(self) -> dict:
        return {
            'posti_disponibili': self.capacita - self.prenotazioni, 
            'economica': self.posti_economica - self.prenotazioni_economica,
            'business': self.posti_business - self.prenotazioni_business,
            'prima': self.posti_prima - self.prenotazioni_prima
        }
    
    def prenota_posto(self, posti: int, classe_servizio: str):
        # prenotazioni_economica = 0
        # prenotazioni_business = 0
        # prenotazioni_prima = 0

        if self.posti_disponibili()['posti_disponibili'] <= 0:
            return "Non ci sono posti disponibili"
        
        if classe_servizio not in ['economica', 'business', 'prima']:
            return "Errore. La classe richiesta non è valida"

        if classe_servizio == 'economica':
            disponibili = self.posti_disponibili()['economica']
            if posti <= disponibili:
                self.prenotazioni_economica += posti
                self.prenotazioni += posti
                print(f"Numero posti prenotati: {posti}. Classe: {classe_servizio}. Codice volo: {self.codice}")
                return "Prenotazion effettuata con successo."
            else:
                return "Non ci sono posti disponibili nella classe economica."

        if classe_servizio == 'business':
            disponibili = self.posti_disponibili()['business']
            if posti <= disponibili:
                self.prenotazioni_business += posti
                self.prenotazioni += posti
                print(f"Numero posti prenotati: {posti}. Classe: {classe_servizio}. Codice volo: {self.codice}")
                return "Prenotazion effettuata con successo."
            else:
                return "Non ci sono posti disponibili nella classe business."

        if classe_servizio == 'prima':
            disponibili = self.posti_disponibili()['prima']
            if posti <= disponibili:
                self.prenotazioni_prima += posti
                self.prenotazioni += posti
                print(f"Numero posti prenotati: {posti}. Classe: {classe_servizio}. Codice volo: {self.codice}")
                return "Prenotazion effettuata con successo."
            else:
                return "Non ci sono posti disponibili nella prima classe."

    

class VoloCharter(Volo):
    def __init__(self, codice: str, capacita: int, costo_volo: float) -> None:
        super().__init__(codice, capacita)
        self.costo_volo = costo_volo 

    def prenota_posto(self):
        if self.posti_disponibili() == self.capacita:
            self.prenotazioni = self.capacita
            print(f"Volo charter {self.codice} prenotato. Prezzo totale: {self.costo_volo*self.prenotazioni} euro.")
        else:
            print(f"Errore. Il volo charter {self.codice} è già prenotato.")

    def posti_disponibili(self):
        return self.capacita - self.prenotazioni if (self.capacita - self.prenotazioni) > 0 else 0
    

class CompagniaAerea:
    def __init__(self, compagnia: str, prezzo_standard: float):
        self.compagnia = compagnia 
        self.prezzo_standard = prezzo_standard
        self.flotta = []

    def aggiungi_volo(self, volo_commerciale: VoloCommerciale):
        self.flotta.append(volo_commerciale)
    
    def rimuovi_volo(self, volo_commerciale: VoloCommerciale):
        if volo_commerciale not in self.flotta:
            raise ValueError("Il volo non è presente nella flotta.")
        else:
            self.flotta.remove(volo_commerciale)
    
    def mostra_flotta(self):
        if not self.flotta:
            print("La flotta è vuota.")
        else: 
            for volo in self.flotta:
                print(f"Codice volo: {volo.codice}")
    
    def guadagno(self) -> float:
        guadagno_totale = 0.0
        for volo in self.flotta:
            posti_disp = volo.posti_disponibili()
            posti_economica = posti_disp['economica']
            posti_business = posti_disp['business']
            posti_prima = posti_disp['prima']

            guadagno_volo = posti_economica*self.prezzo_standard + posti_business*(self.prezzo_standard*2) + posti_prima*(self.prezzo_standard*3)

            guadagno_totale += round(guadagno_volo, 2)
        return guadagno_totale
    

if __name__ == '__main__':

    print("Posti dispnibili sul volo commerciale: ")
    volo1 = VoloCommerciale("2569", 100)
    print(volo1.posti_disponibili())

    volo1.prenota_posto(70, 'economica')
    print(volo1.posti_disponibili())

    volo1.prenota_posto(20, 'business')
    print(volo1.posti_disponibili())
    
    volo1.prenota_posto(70, 'economica')
    print(volo1.posti_disponibili())

    volo1.prenota_posto(10, 'prima')
    print(volo1.posti_disponibili())

    volo1.prenota_posto(11, 'prima')
    print(volo1.posti_disponibili())


    volocharter = VoloCharter("58965", 200, 120)
    volocharter.prenota_posto()
    volocharter.prenota_posto()

    volo2 = VoloCommerciale("LO8659", 200)
    volo2.prenota_posto(30, 'economica')

    ryanair = CompagniaAerea("Ryanair", 95)
    ryanair.aggiungi_volo(volo2)
    ryanair.aggiungi_volo(volo1)
    print("Ecco la flotta della compagnia aerea Ryanair:")
    ryanair.mostra_flotta()
    print(f"Dalla vendita dei biglietti aerei, la compagnia aerea Ryanair ha guadagnato {ryanair.guadagno()} euro")