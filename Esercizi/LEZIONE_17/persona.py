class Persona:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.__first_name = None
        self.__last_name = None 
        self.__age = None
        
        if not isinstance(first_name, str):
            print("Il nome inserito non è una stringa!")
        else: 
            self.__first_name = first_name

        if not isinstance(last_name, str):
            print("Il cognome inserito non è una stringa!")
        else: 
            self.__last_name = last_name

        if self.__first_name is not None and self.__last_name is not None:
            self.__age = 0
        else:
            self.__age = None

    def setFirstName(self, first_name: str | None) -> None:
        if not isinstance(first_name, str):
            print("Il nome inserito non è una stringa!")
        self.__first_name = first_name
    
    def getFirstName(self) -> str | None:
        return self.__first_name 
    
    def setLastName(self, last_name: str | None) -> None:
        if not isinstance(last_name, str):
            print("Il cognome inserito non è una stringa!")
        self.__last_name = last_name 
    
    def getLastName(self) -> str | None:
        return self.__last_name

    def setAge(self, age: int) -> None:
        if not isinstance(age, int):
            print("L'età deve essere un numero intero!")
        else:
            self.__age = age  

    def getAge(self) -> int | None:
        return self.__age 
    
    def greet(self) -> str:
        print(f"Ciao, sono {self.getFirstName()} {self.getLastName()}! Ho {self.getAge()} anni!")

persona1 = Persona("Lisa", "Bini")
persona1.setAge(22)
persona1.greet()