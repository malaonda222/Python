'''Esercizio 3 - Sistema di gestione veicoli
Obiettivo: Applicare classi astratte per creare una gerarchia più realistica e polimorfica.
Nome dell’esercizio: Veicolo
Traccia:
Crea una classe astratta Veicolo con:
attributi: marca, modello, anno
metodi astratti: avvia(), ferma(), descrizione()
Crea tre sottoclassi:
Auto
Moto
Camion
Ognuna deve implementare i tre metodi astratti con messaggi personalizzati (es. "L’auto Toyota Corolla è partita.").
Crea una lista di veicoli diversi e scrivi una funzione che li avvii tutti e poi li fermi tutti, usando solo metodi della classe base.
Suggerimento: usa il polimorfismo: non serve controllare il tipo di veicolo.'''

from abc import ABC, abstractmethod

class Veicolo(ABC):
    def __init__(self, marca: str, modello: str, anno: int) -> None:
        self.marca = marca 
        self.modello = modello
        self.anno = anno 
    
    @abstractmethod
    def avvia(self) -> None:
        pass 

    @abstractmethod
    def ferma(self) -> None:
        pass 

    @abstractmethod
    def descrizione(self) -> None:
        pass 

class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int) -> None:
        super().__init__(marca, modello, anno) 
    
    def avvia(self) -> None:
        print(f"L'auto {self.marca} {self.modello} è partita.")

    def ferma(self) -> None:
        print(f"L'auto {self.marca} {self.modello} si è fermata.")
    
    def descrizione(self) -> None:
        print(f"Auto: {self.marca} - Modello: {self.modello} - Anno: {self.anno}")

class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int) -> None:
        super().__init__(marca, modello, anno)

    def avvia(self) -> None:
        print(f"La moto {self.marca} {self.modello} è partita.")

    def ferma(self) -> None:
        print(f"La moto {self.marca} {self.modello} si è fermata.")
    
    def descrizione(self) -> None:
        print(f"Moto: {self.marca} - Modello: {self.modello} - Anno: {self.anno}")

class Camion(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int) -> None:
        super().__init__(marca, modello, anno)

    def avvia(self) -> None:
        print(f"Il camion {self.marca} {self.modello} è partito.")

    def ferma(self) -> None:
        print(f"Il camion {self.marca} {self.modello} si è fermato.")
    
    def descrizione(self) -> None:
        print(f"Camion: {self.marca} - Modello: {self.modello} - Anno: {self.anno}")

auto1 = Auto("Toyota", "Yaris", 2010) 
auto2 = Auto("Fiat", "500x", 2008)
moto1 = Moto("Aprilia", "500Rider", 2014)
moto2 = Moto("Motoguzzi", "Stelvio", 2009)
camion1 = Camion("Iveco", "Combo", 2008)
camion2 = Camion("Volvo", "Jiso", 2025)

lista_veicoli = [auto1, auto2, moto1, moto2, camion1, camion2]

for veicolo in lista_veicoli:
    veicolo.avvia()

for veicolo in lista_veicoli:
    veicolo.ferma()