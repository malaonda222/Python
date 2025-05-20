from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def __init__(self, name:str, surname: str, cf: str, age: int):
        self._name = name
        self._surname = surname 
        self._cf = cf
        self._age = age
    
    def set_name(self, nome: str):
        self._name = nome 
    
    def get_name(self) -> str:
        return self._nome 
    
    def get_lista(self) -> list:
        return self.lista 
    
if __name__ == '__main__':
    p = Person('Giovanni', 'Rossi', 'irhfjgiejdppoo')
    p.add_elem(10)
