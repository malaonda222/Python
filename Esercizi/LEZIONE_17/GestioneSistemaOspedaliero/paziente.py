from Esercizi.LEZIONE_17.GestioneSistemaOspedaliero.persona import Persona 

class Paziente(Persona):
    def __init__(self, first_name: str, last_name: str, idCode: str) -> None:
        super().__init__(first_name, last_name)
        if not isinstance(idCode, str):
            print("Errore. Codice identificativo non valido")
            self.__idCode = None
        else:
            self.__idCode = idCode

    def setIdCode(self, idCode: str) -> None:
        if not isinstance(idCode, str):
            print("Errore. Codice identificativo non valido")
        else:
            self.__idCode = idCode
    
    def getIdCode(self) -> str | None:
        return self.__idCode
    
    def patientInfo(self) -> None:
        print(f"Paziente: {self.getFirstName()} {self.getLastName()}\nID: {self.getIdCode()}")


paziente1 = Paziente("Erica", "Dassi", "rhg89")
paziente1.patientInfo()