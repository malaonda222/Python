from Esercizi.LEZIONE_17.GestioneSistemaOspedaliero.dottore import Dottore 
from Esercizi.LEZIONE_17.GestioneSistemaOspedaliero.paziente import Paziente
from Esercizi.LEZIONE_17.GestioneSistemaOspedaliero.persona import Persona 

class Fattura: 
    def __init__(self, patient: list[Paziente], doctor: Dottore) -> None:        
        if doctor.isAValidDoctor():
            self.patient = patient if patient is not None else []
            self.doctor = doctor 
            self.fatture = len(self.patient)
            self.salary = 0
        else:
            self.patient = None
            self.doctor = None 
            self.fatture = None 
            self.salary = None 
            print("Non è possibile creare la classe fattura poiché il dottore non è valido!")
        
    def getSalary(self) -> float | None:
        if self.doctor is not None and self.patient is not None:
            self.salary = self.doctor.getParcel() * len(self.patient)
            return self.salary
        return None 
    
    def getFatture(self):
        if self.patient is not None:
            self.fatture = len(self.patient)
            return self.fatture
        return None 
    
    def addPatient(self, newPatient: Paziente) -> None:
        if not isinstance(newPatient, Paziente):
            raise ValueError("Errore. L'oggetto non è un paziente")
        else: 
            self.patient.append(newPatient)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {self.doctor.getLastName()} è stato aggiunto il paziente {newPatient.getIdCode()}")
    
    def removePatient(self, idCode: str) -> None:
        paziente_trovato = None
        for paziente in self.patient:
            if paziente.getIdCode() == idCode:
                paziente_trovato = paziente
                break  
        if paziente_trovato is None:
            print("Errore. Il paziente non è presente nella lista")
        else:
            self.patient.remove(paziente_trovato)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {self.doctor.getLastName()} è stato rimosso il paziente {paziente_trovato.getIdCode()}")


    def remove(self, idCode: str) -> None:
        trovato = None 
        for paziente in self.patient:
            if paziente.getIdCode() == idCode:
                trovato = paziente
                break 
        if trovato is None:
            print("Il paziente non è presente nella lista")
        else:
            self.patient.remove(trovato)
            self.getFatture()
            self.salary = self.getSalary()
            doctor_cognome = self.doctor.getLastName() if self.doctor else "Sconosciuto"
            print(f"Alla lista del Dottor {doctor_cognome} è stato rimosso il paziente {idCode}")

