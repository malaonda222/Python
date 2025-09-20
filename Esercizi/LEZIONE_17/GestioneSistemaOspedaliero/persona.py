class Persona:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.setFirstName(first_name)
        self.setLastName(last_name)

        if self.getFirstName() is not None and self.getLastName() is not None:
            self.__age = 0
        else:
            self.__age = None 

    def setFirstName(self, first_name: str | None) -> None:
        if not isinstance(first_name, str):
            print("Il nome inserito non è una stringa!")
            self.__first_name = None
        else: 
            self.__first_name = first_name
    
    def getFirstName(self) -> str | None:
        return self.__first_name 
    
    def setLastName(self, last_name: str | None) -> None:
        if not isinstance(last_name, str):
            print("Il cognome inserito non è una stringa!")
            self.__last_name = None
        else: 
            self.__last_name = last_name
    
    def getLastName(self) -> str | None:
        return self.__last_name

    def setAge(self, age: int) -> None:
        if age is None:
            self.__age = None 
        elif not isinstance(age, int) or age < 0:
            print("L'età deve essere un numero intero positivo!")
        else:
            self.__age = age  

    def getAge(self) -> int | None:
        return self.__age 
    
    def greet(self) -> None:
        print(f"Ciao, sono {self.getFirstName()} {self.getLastName()}! Ho {self.getAge()} anni!")

persona1 = Persona("Lisa", "Bini")
persona1.setAge(22)
persona1.greet()