from forma_generica import FormaGenerica

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


