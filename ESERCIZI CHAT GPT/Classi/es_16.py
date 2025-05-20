'''
Crea una classe Animale con:
Attributi: nome, specie
Metodo: parla() che stampa una frase tipo:
"L'animale Cane di nome Fido fa un verso."
'''

class Animale:
    def __init__(self, nome:str, specie:str):
        self.nome = nome
        self.specie = specie 
    
    def parla(self):
        versi = {
            "cane": "bau",
            "gatto": "miao",
            "mucca": "muu",
            "pecora": "bee"
        }
        verso = versi.get(self.specie, "un verso non ben definito")
        print(f"L'animale {self.specie} di nome {self.nome} fa {verso}.")
    
animale = Animale("Fido", "cane")
animale.parla()

animale_1 = Animale("Rick", "gatto")
animale_1.parla()

animale1 = Animale("Furia", "delfino")
animale1.parla()