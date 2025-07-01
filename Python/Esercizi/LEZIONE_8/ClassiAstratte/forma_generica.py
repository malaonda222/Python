from abc import ABC, abstractmethod #abstract base class

#classe FormaGenerica astratta
class FormaGenerica(ABC):

    #metodo astratto della classe FormaGenerica
    @abstractmethod #decorator per indicare che quel metodo è astratto
    def draw(self) -> None:
        pass 

    #definire il set e il get
    def setShape(self, shape: str) -> None:
        if not isinstance(shape, str) or shape.strip() == "": #controlla che sia una stringa oppure che la stringa non sia vuota
            raise ValueError(f"Errore. \"Shape\" deve essere una stringa e non deve essere vuota.")
        else:
            self.shape = shape #imposta attributo della stringa shape con il valore della stringa shape
        
    def getShape(self) -> str:
        return self.shape 

#creazione di una sottoclasse Rettangolo
class Rettangolo(FormaGenerica):
    #inizializzare un oggetto della classe rettangolo
    def __init__(self):
        super().__init__()

        self.setShape('Rettangolo')

    def draw(self) -> None:

        print(f"\n{self.getShape()}\n")

        #outer ciclo for per le righe 
        for i in range(5):
            #inner for per le colonne 
            for j in range(5*2):

                #lato a e lato d del rettangolo
                if i == 0 or i == 5-1:
                    print("*", end=" ")
                #lato b e lato c del rettangolo
                elif j == 0 or j == (5*2)-1:
                    print("*", end=" ")
                #stampa spazi bianchi 
                else:
                    print(" ", end=" ")

            print("\n", end="") #quando si finisce il ciclo j, vammi a capo e metti una stringa vuota 


#creo un oggetto r della classe Rettangolo 
r: Rettangolo = Rettangolo()
r.draw()