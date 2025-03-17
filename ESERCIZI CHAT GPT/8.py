# Veicolo
class Veicolo:
    def __init__ (self, ruote:int, a_motore:bool):
        self.ruote = ruote
        self.a_motore = a_motore 
    
class Auto(Veicolo):
    def __init__(self, marca:str, modello:str):
        self.ruote = 4
        self.a_motore = True
        self.marca = marca 
        self.modello = modello 

class Moto(Veicolo):
    def __init__(self, marca:str, modello:str):
        self.ruote = 2
        self.a_motore = False 
        self.marca = marca 
        self.modello = modello 

class Bicicletta(Veicolo):
    def __init__(self, tipo:str):
        self.ruote = 2
        self.a_motore = False 
        self.tipo = tipo 

veicolo1 = Auto(marca="Audi", modello="A3")
veicolo2 = Moto(marca="Moto Guzzi", modello="Stelvio")
veicolo3 = Bicicletta(tipo="da città")

for veicolo in [veicolo1, veicolo2, veicolo3]:
    match veicolo:
        case Auto(marca, modello):
            print(f"Veicolo: Auto | Marca: {marca}, Modello: {modello}, Ruote: {veicolo.ruote}, Motore: {veicolo.a_motore}")
        case Moto(marca, modello):
            print(f"Veicolo: Moto | Marca: {marca}, Modello: {modello}, Ruote: {veicolo.ruote}, Motore: {veicolo.a_motore}")
        case Bicicletta(tipo):
            print(f"Veicolo: Bicicletta | Tipo: {tipo}, Ruote: {veicolo.ruote}, Motore: {veicolo.a_motore}")
        case _:
            print("Tipo di veicolo sconosciuto.")