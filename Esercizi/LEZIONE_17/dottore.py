from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)
        self.__specialization = None
        self.__parcel = None 

        if not isinstance(specialization, str):
            print("La specializzazione inserita non è una stringa")
        else:
            self.__specialization = specialization

        if not isinstance(parcel, float):
            print("La parcella inserita non è un float!")
        else:
            self.__parcel = parcel 

    def setSpecialization(self, specialization: str) -> None:
        if not isinstance(specialization, str):
            print("La specializzazione insertia non è una stringa!")
        else:
            self.__specialization = specialization
    
    def getSpecialization(self) -> str | None:
        return self.__specialization
    
    def setParcel(self, parcel: float) -> None:
        if not isinstance(parcel, float):
            print("La parcella inserita non è un float!")
        else:
            self.__parcel = parcel 

    def getParcel(self) -> float | None:
        return self.__parcel 
    
    def isAValidDoctor(self) -> str:
        if self.getAge() > 30:
            print(f"Doctor {self.getFirstName()} {self.getLastName()} is valid!")
        else:
            print(f"Doctor {self.getFirstName()} {self.getLastName()} is not valid!")
    
    def doctorGreet(self) -> str:
        self.greet()
        print(f"Sono un medico {self.getSpecialization()}")

ginecologo = Dottore("Silvano", "Belli", "ginecologo", 1500.099)
ginecologo.setAge(45)
ginecologo.isAValidDoctor()
ginecologo.doctorGreet()