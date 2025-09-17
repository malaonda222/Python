from dottore import Dottore 
from paziente import Paziente
from persona import Persona 

class Fattura: 
    def __init__(self, patient: list[Paziente], doctor: Dottore) -> None:
        self.doctor = doctor 
        self.patient = patient if patient is not None else []
        
        if doctor.isAValidDoctor():
            self.fatture = len(self.__patient)
            self.salary = 0
        else:
            self.patient = None
            self.doctor = None 
            self.fatture = None 
            self.salary = None 
            print("Non è possibile creare la classe fattura poiché il dottore non è valido!")
        
    def getSalary(self) -> float:
        if self.doctor is not None and self.patient is not None:
            return self.doctor.getParcel() * len(self.patient)
        return None 
    
    def getFatture(self):
        if self.patient is not None:
            self.fatture = len(self.patient)
            return self.fatture
        return None 
    
    def addPatient(self, newPatient: Paziente) -> str:
        if not isinstance(newPatient, Paziente):
            raise ValueError("Errore. L'oggetto non è un paziente")
        else: 
            self.patient.append(newPatient)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {self.doctor} è stato aggiunto il paziente {Paziente.getIdCode()}")
    
    def removePatient(self, idCode: str):
        if idCode not in self.patient:
            print("Errore. Il paziente non è presente nella lista")
        else:
            self.patient.remove(idCode)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {self.doctor} è stato rimosso il paziente {Paziente.getIdCode()}")


