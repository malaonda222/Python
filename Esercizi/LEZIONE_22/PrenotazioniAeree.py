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
    def __init__(self, codice: str, capacita: int, posti_economica = 0, posti_business = 0, posti_prima = 0):
        super().__init__(codice, capacita)
 
        self.posti_economica = int(posti_economica) if posti_economica > 0 else int(capacita * 0.7)
        self.posti_business = int(posti_business) if posti_business > 0 else int(capacita * 0.2)
        self.posti_prima = int(posti_prima) if posti_prima > 0 else int(capacita * 0.1)
 
        self.prenotazioni_economica = 0
        self.prenotazioni_business = 0
        self.prenotazioni_prima = 0

    def posti_disponibili(self) -> dict:
        posti_disponibili = {
            'posti_disponibili': (self.capacita - self.prenotazioni) if (self.capacita - self.prenotazioni) > 0 else 0,
            'economica': (self.posti_economica - self.prenotazioni_economica) if (self.posti_economica - self.prenotazioni_economica) > 0 else 0,
            'business': (self.posti_business - self.prenotazioni_business) if (self.posti_business - self.prenotazioni_business) > 0 else 0,
            'prima': (self.posti_prima - self.prenotazioni_prima) if (self.posti_prima - self.prenotazioni_prima) > 0 else 0
        }
        return posti_disponibili
    
    def prenota_posto(self, posti: int, classe_servizio: str):
        if (self.capacita - self.prenotazioni) <= 0:
            return f"Il volo è al completo.\n"
        
        if classe_servizio not in ['economica', 'business', 'prima']:
            return "Errore. La classe richiesta non è valida\n"

        posti_disponibili = self.posti_disponibili()

        if classe_servizio == 'economica':
            if posti_disponibili['economica'] <= 0:
                return f"Non ci sono posti disponibili nella classe economica del volo {self.codice}\n"
            
            if posti > posti_disponibili['economica']:
                return f"Non è possibile riservare {posti} posti nella classe economica. Numero posti disponibili: {posti_disponibili['economica']}\n"

            self.prenotazioni_economica += posti
            self.prenotazioni += posti
            print(f"Numero posti prenotati: {posti}. Classe: {classe_servizio}. Codice volo: {self.codice}")
       

        if classe_servizio == 'business':
            if posti_disponibili['business'] <= 0:
                return f"Non ci sono posti disponibili nella classe business del volo {self.codice}"
            
            if posti > posti_disponibili['business']:
                return f"Non è possibile riservare {posti} posti nella classe business. Numero posti disponibili: {posti_disponibili['business']}"

            self.prenotazioni_business += posti
            self.prenotazioni += posti
            print(f"Numero posti prenotati: {posti}. Classe: {classe_servizio}. Codice volo: {self.codice}")
       

        if classe_servizio == 'prima':
            if posti_disponibili['prima'] <= 0:
                return f"Non ci sono posti disponibili nella classe prima del volo {self.codice}"
            
            if posti > posti_disponibili['prima']:
                return f"Non è possibile riservare {posti} posti nella classe prima. Numero posti disponibili: {posti_disponibili['prima']}" 

            self.prenotazioni_prima += posti
            self.prenotazioni += posti
            print(f"Numero posti prenotati: {posti}. Classe: {classe_servizio}. Codice volo: {self.codice}")
    

class VoloCharter(Volo):
    def __init__(self, codice: str, capacita: int, costo_volo: float) -> None:
        super().__init__(codice, capacita)
        self.costo_volo = costo_volo 

    def posti_disponibili(self):
        return (self.capacita - self.prenotazioni) if (self.capacita - self.prenotazioni) > 0 else 0

    def prenota_posto(self):
        if self.posti_disponibili() == self.capacita:
            self.prenotazioni = self.capacita
            return f"Volo charter {self.codice} prenotato. Prezzo totale: {self.costo_volo*self.prenotazioni} euro."
        else:
            return f"Il volo charter {self.codice} è già prenotato.\n"

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
            return "La flotta è vuota."
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

    report: list = []

    volo1 = VoloCommerciale("COM123", 100)
    messaggio1 = "Posti disponibili sul volo commerciale: "
    report.append(messaggio1)
    report.append(str(volo1.posti_disponibili()))
    
    messaggio2 = volo1.prenota_posto(70, 'economica')
    report.append(messaggio2)
    print(str(volo1.posti_disponibili()))

    messaggio3 = volo1.prenota_posto(20, 'business')
    report.append(messaggio3)
    print(str(volo1.posti_disponibili()))
    
    messaggio4 = volo1.prenota_posto(70, 'economica')
    report.append(messaggio4)
    print(str(volo1.posti_disponibili()))

    messaggio5 = volo1.prenota_posto(10, 'prima')
    report.append(messaggio5)
    print(str(volo1.posti_disponibili()))


    report.append(str(volo1.posti_disponibili()))
    print(str(volo1.posti_disponibili()))
    print()

    volocharter = VoloCharter("CHA456", 200, 100)
    print(f"Posti disponibili su volo charter {volocharter.codice}: {volocharter.posti_disponibili()}")
    print(volocharter.prenota_posto())
    print(volocharter.prenota_posto())

    volo2 = VoloCommerciale("COM456", 143)
    messaggio7 = volo2.prenota_posto(100, 'economica')
    report.append(messaggio7)
    
    print()
    ita = CompagniaAerea("ITA", 124)
    ita.aggiungi_volo(volo1)
    ita.aggiungi_volo(volo2)

    messaggio11 = "Ecco la flotta della compagnia aerea ITA:"
    print(messaggio11)
    messaggio12 = ita.mostra_flotta()
    report.append(messaggio12)
    
    print()
    messaggio13 = f"Dalla vendita dei biglietti aerei, la compagnia aerea Ryanair ha guadagnato {ita.guadagno()} euro"
    report.append(messaggio13)
    print(messaggio13)


    with open("report.txt", "a") as file:
        for messaggio in report:
            file.write(str(messaggio) + "\n")
