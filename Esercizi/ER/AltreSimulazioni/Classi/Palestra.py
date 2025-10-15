'''
Esercizio: Sistema di Gestione di una Palestra Digitale
Implementa tre classi interagenti per gestire l’iscrizione ai corsi di fitness.
 
1. Classe FitnessClass
Rappresenta un corso di fitness offerto dalla palestra.
 
A. Attributi:
 
* class_id: str
* name: str
* time_slot: str (es. "18:00-19:00")
* is_full: bool
 
B. Metodi:
 
    * book_spot() -> None
    Se is_full è False, lo imposta a True; altrimenti stampa:
    "Il corso '{self.name}' alle '{self.time_slot}' è già al completo."
 
    * cancel_booking() -> None
    Se is_full è True, lo imposta a False; altrimenti stampa:
    "Il corso '{self.name}' alle '{self.time_slot}' non ha prenotazioni da cancellare."
 
2. Classe Member
 
A. Attributi:
 
* member_id: str
* name: str
* booked_classes: list[FitnessClass]
 
B. Metodi:
 
    * book_class(course: FitnessClass) -> None
    Se il corso non è pieno, lo aggiunge a booked_classes e chiama course.book_spot().
    Altrimenti stampa:
    "Il corso '{course.name}' non è disponibile per la prenotazione."
 
    * cancel_class(course: FitnessClass) -> None
    Se il corso è in booked_classes, lo rimuove e chiama course.cancel_booking().
    Altrimenti stampa:
    "Il corso '{course.name}' non era prenotato da questo membro."
 
3. Classe Gym
 
A. Attributi:
 
* classes: dict[str, FitnessClass]
* members: dict[str, Member]
 
B. Metodi:
 
    * add_class(class_id: str, name: str, time_slot: str) -> None
    Se class_id esiste già, stampa:
    "Il corso con ID '{class_id}' esiste già."
    Altrimenti crea e aggiunge un nuovo FitnessClass.
 
    * register_member(member_id: str, name: str) -> None
    Se member_id esiste già, stampa:
    "Il membro con ID '{member_id}' è già registrato."
    Altrimenti crea e aggiunge un nuovo Member.
 
    * book_class_for_member(member_id: str, class_id: str) -> None
    Se entrambi esistono, invoca member.book_class(course)
    Altrimenti stampa:
    "Membro o corso non trovato."
 
    * cancel_class_for_member(member_id: str, class_id: str) -> None
    Se entrambi esistono, invoca member.cancel_class(course)
    Altrimenti stampa:
    "Membro o corso non trovato."
 
    * list_available_classes() -> list[str]
    Restituisce una lista di class_id non pieni.
 
    * list_member_bookings(member_id: str) -> list[str] | str
    Se il membro esiste, restituisce una lista di class_id prenotati.
    Altrimenti restituisce:
    "Errore: membro non trovato."
'''

class FitnessClass:
    def __init__(self, class_id: str, name: str, time_slot: str) -> None:
        self.class_id: str = class_id
        self.name: str = name 
        self.time_slot: str = time_slot
        self.is_full: bool = False 

    def book_spot(self) -> None:
        if not self.is_full:
            self.is_full = True
        else:
            print(f"Il corso '{self.name}' alle '{self.time_slot}' è già al completo.")
    
    def cancel_booking(self) -> None:
        if self.is_full:
            self.is_full = False
        else:
            print(f"Il corso '{self.name}' alle '{self.time_slot}' non ha prenotazioni da cancellare.")


class Member:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id: str = member_id
        self.name: str = name
        self.booked_classes: list[FitnessClass] = []

    def book_class(self, course: FitnessClass) -> None:
        if course.is_full == False:
            self.booked_classes.append(course)
            course.book_spot()
        else:
            print(f"Il corso '{course.name}' non è disponibile per la prenotazione.")
    
    def cancel_class(self, course: FitnessClass) -> None:
        if course in self.booked_classes:
            self.booked_classes.remove(course)
            course.cancel_booking()
        else:
            print(f"Il corso '{course.name}' non era prenotato da questo membro.")


class Gym:
    def __init__(self) -> None:
        self.classes: dict[str, FitnessClass] = {}
        self.memebers: dict[str, Member] = {}

    def add_class(self, class_id: str, name: str, time_slot: str) -> None:
        if class_id in self.classes:
            print(f"Il corso con ID")