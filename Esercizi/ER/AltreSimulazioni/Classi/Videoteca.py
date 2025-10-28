'''Esercizio: Gestione di una Videoteca
Obiettivo
Creare un sistema per gestire film, utenti e noleggi in una videoteca.

Classi richieste:

1. Classe Film
Rappresenta un film. Deve avere:

 *titolo: stringa
 *regista: stringa
 *anno: int
 *disponibile: booleano (True se non è in prestito)

Metodi:
- __init__
- noleggia() → imposta disponibile a False
- restituisci() → imposta disponibile a True
- __str__() → restituisce qualcosa tipo "Titolo" di Regista (Disponibile/Non disponibile)

2. Classe Utente
Rappresenta un utente della videoteca. Deve avere:

 *nome: stringa
 *id_utente: stringa
 *film_in_prestito: lista di oggetti Film

Metodi:
- __init__
- prendi_in_prestito(film: Film) → aggiunge il film a film_in_prestito e lo marca come non disponibile
- restituisci_film(film: Film) → rimuove il film da film_in_prestito e lo marca come disponibile
- __str__() → mostra il nome dell’utente e i titoli dei film in prestito


3. Classe Videoteca
Rappresenta la videoteca. Deve avere:

 *film: dizionario di oggetti Film, chiave: titolo o ID
 *utenti: dizionario di oggetti Utente, chiave: ID utente

Metodi:
- aggiungi_film(film: Film)
- aggiungi_utente(utente: Utente)
- noleggia_film(id_utente: str, titolo_film: str) → permette all’utente di prendere un film se disponibile
- restituisci_film(id_utente: str, titolo_film: str) → permette all’utente di restituire un film
- lista_film_disponibili() → restituisce i film che sono disponibili'''

class Film:
    def __init__(self, titolo: str, regista: str, anno: int) -> None:
        self.titolo: str = titolo 
        self.regista: str = regista 
        self.anno: int = anno 
        self.disponibile: bool = True 
    
    def noleggia(self) -> None:
        if self.disponibile:
            self.disponibile = False 
        else:
            print(f"Film {self.titolo}' non disponibile")

    def restituisci(self) -> None:
        if not self.disponibile:
            self.disponibile = True 
        else:
            print(f"Film '{self.titolo} disponibile")
    
    def __str__(self) -> str:
        return f"'{self.titolo}' di '{self.regista}': ({self.disponibile})"

class Utente:
    def __init__(self, nome: str, id_utente) -> None:
        self.nome: str = nome 
        self.id_utente: str = id_utente
        self.film_in_prestito: list[Film] = []
    
    def prendi_in_prestito(self, film: Film) -> None:
        if film not in self.film_in_prestito:
            self.film_in_prestito.append(film)
            film.noleggia()
        else:
            return "Il film è già stato preso in prestito dall'utente"
    
    def restituisci_film(self, film: Film) -> None:
        if film in self.film_in_prestito:
            self.film_in_prestito.remove(film)
            film.restituisci()
        else:
            return "Film non presente nella lista dei film presi in prestito"
    
    def __str__(self) -> str:
        return f"Nome utente: {self.nome} - Film in prestito: {self.film_in_prestito}"

class Videoteca:
    def __init__(self) -> None:
        self.films: dict[str, Film] = {}
        self.utenti: dict[str, Utente] = {}

    def aggiungi_film(self, film: Film) -> None:
        if film.titolo not in self.films:
            self.films[film.titolo] = film 
        else:
            print(f"Film '{film.titolo}' già presente nel dizionario dei film")
    
    def aggiungi_utente(self, utente: Utente) -> None:
        if utente.id_utente not in self.utenti:
            self.utenti[utente.id_utente] = utente 
        else:
            print(f"Utente '{utente.id_utente}' già presente nel dizionario degli utenti")

    def noleggia_film(self, id_utente, titolo_film: str) -> None:
        if id_utente in self.utenti and titolo_film in self.films:
            utente = self.utenti[id_utente]
            film = self.films[titolo_film]
            utente.prendi_in_prestito(film)
        else:
            return "Utente o film non trovati"

    def restituisci_film(self, id_utente: str, titolo_film: str) -> None:
        if id_utente in self.utenti and titolo_film in self.films:
            utente = self.utenti[id_utente]
            film = self.films[titolo_film]
            utente.restituisci_film(film)
        else:
            return "Utente o film non trovati"
    
    def lista_film_disponibili(self) -> None: #restituisce i film che sono disponibili
        if not self.films:
            return "La lista dei film è vuota"
        else:
            film_disponibili = []
            for film in self.films.values():
                if film.disponibile:
                    film_disponibili.append(film.titolo)
            return f'I film disponibili sono i seguenti: {", ".join(film_disponibili)}'

film1 = Film("Ciao Amore", "Buzzi", 2022)
film2 = Film("Sei", "Minni", 1998)
film3 = Film("356", "Binelli", 2003)

utente1 = Utente("Lisa", "12345")

utente1.prendi_in_prestito(film1)

videoteca = Videoteca()

videoteca.aggiungi_film(film1)
videoteca.aggiungi_film(film2)
videoteca.aggiungi_film(film3)

print(videoteca.lista_film_disponibili())




