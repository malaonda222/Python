class Veicolo:
    def __init__(self, marca: str, modello: str, anno: int):
        self.marca = marca 
        self.modello = modello
        self.anno = anno 

    def descrivi_veicolo(self):
        return f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}"

    def __str__(self):
        print(self.descrivi_veicolo())

class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    def descrivi_veicolo(self):
        print(super().descrivi_veicolo()), f", Numero di porte: {self.numero_porte}"

class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, tipo: str):
        super().__init__(marca, modello, anno)
        self.tipo = tipo 

    def descrivi_veicolo(self):
        print(super().descrivi_veicolo()), f", Tipo: {self.tipo}"

        
veicolo = Veicolo("Generic", "Model", 2020)  # Crea un'istanza della classe Veicolo
auto = Auto("Toyota", "Corolla", 2021, 4)  # Crea un'istanza della classe Auto
moto = Moto("Yamaha", "R1", 2022, "sportiva")  # Crea un'istanza della classe Moto

veicolo.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Veicolo
auto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Auto
moto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Moto


