from Esercizi.LEZIONE_17.GestioneSistemaOspedaliero.persona import Persona

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)
        self.setSpecialization(specialization)
        self.setParcel(parcel)

    def setSpecialization(self, specialization: str) -> None:
        if not isinstance(specialization, str):
            print("La specializzazione inserita non è una stringa")
            self.__specialization = None
        else:
            self.__specialization = specialization
    
    def getSpecialization(self) -> str | None:
        return self.__specialization
    
    def setParcel(self, parcel: float) -> None:
        if not isinstance(parcel, float):
            print("La parcella inserita non è un float!")
            self.__parcel = None 
        else:
            self.__parcel = parcel 

    def getParcel(self) -> float | None:
        return self.__parcel 
    
    def isAValidDoctor(self) -> bool:
        if self.getAge() is None:
            print("Età non specificata. Impossibile determinare la validità del dottore")
            return False
        if self.getAge() > 30:
            print(f"Doctor {self.getFirstName()} {self.getLastName()} is valid!")
            return True
        else:
            print(f"Doctor {self.getFirstName()} {self.getLastName()} is not valid!")
            return False
    
    def doctorGreet(self) -> None:
        self.greet()
        if self.getSpecialization() is None:
            print("Non ho una specializzazione")
        else:
            print(f"Sono un medico {self.getSpecialization()}")

ginecologo = Dottore("Silvano", "Belli", "ginecologo", 1500.099)
ginecologo.setAge(45)
ginecologo.isAValidDoctor()
ginecologo.doctorGreet()