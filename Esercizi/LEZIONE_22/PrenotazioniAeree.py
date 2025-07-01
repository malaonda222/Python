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
        posti_disponibili_totali = {
            'posti_disponibili': self.capacita - self.prenotazioni if (self.capacita - self.prenotazioni) > 0 else 0, 
            'economica': self.posti_economica - self.prenotazioni_economica if (self.posti_economica - self.prenotazioni_economica) > 0 else 0,
            'business': self.posti_business - self.prenotazioni_business if (self.posti_business - self.prenotazioni_business) > 0 else 0,
            'prima': self.posti_prima - self.prenotazioni_prima if (self.posti_prima - self.prenotazioni_prima) > 0 else 0
        }
        return posti_disponibili_totali
    
    def prenota_posto(self, posti: int, classe_servizio: str):
        prenotazioni_economica = 0
        prenotazioni_business = 0
        prenotazioni_prima = 0

        if (self.capacita - self.prenotazioni) <= 0:
            return "Non ci sono posti disponibili"
        if classe_servizio not in ['classe_economica', 'classe_business', 'classe_prima']:
            print("Errore. La classe richiesta non è valida.")

        if classe_servizio == 'economica':
            if posti <= self.posti_economica:
                self.posti_economica -= posti
                self.prenotazioni_economica = posti 
            else:
                print("Non ci sono posti disponibili nella classe economica")

        if classe_servizio == 'business':
            if posti <= self.posti_business:
                self.posti_business -= posti
                self.prenotazioni_business = posti 
            else:
                print("Non ci sono posti disponibili nella classe business")

        if classe_servizio == 'prima':
            if posti <= self.posti_prima:
                self.posti_prima -= posti
                self.prenotazioni_prima = posti 
            else:
                print("Non ci sono posti disponibili nella prima classe")
                
        self.prenotazioni += posti
        self.prenotazioni_economica += prenotazioni_economica
        self.prenotazioni_business += prenotazioni_business
        self.prenotazioni_prima += prenotazioni_prima
        
        print(f"Numero posti prenotati: {posti}. Classe: {classe_servizio}. Codice volo: {self.codice}")
        return "Prenotazione effettuata con successo."
    

class VoloCharter(Volo):
    def __init__(self, codice: str, capacita: int, costo_volo: float) -> None:
        super().__init__(codice, capacita)
        self.costo_volo = costo_volo 

    def prenota_posto(self):
        if self.posti_disponibili() == self.capacita:
            self.prenotazioni = self.capacita
            print(f"Volo charter {self.codice} prenotato. Prezzo totale: {self.costo_volo*self.prenotazioni} euro.")
        else:
            print(f"Il volo charter {self.codice} è già prenotato.")

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
            # posti_disp = volo.posti_disponibili() oppure
            posti_economica = volo.posti_disponibili['economica']
            posti_business = volo.posti_disponibili['business']
            posti_prima = volo.posti_disponibili['prima']

            guadagno_volo = posti_economica*self.prezzo_standard + posti_business*(self.prezzo_standard*2) + posti_prima*(self.prezzo_standard*3)

            guadagno_totale += round(guadagno_volo, 2)
