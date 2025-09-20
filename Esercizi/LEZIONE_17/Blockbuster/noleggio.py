from __future__ import annotations
from film import Film 
from movie_genre import Azione, Commedia, Drama  

class Noleggio:
    def __init__(self, film_list: list[Azione|Commedia|Drama] = None) -> None:
        self.film_list = film_list if film_list is not None else []
        self.rented_film = dict()

    def isAvailable(self, film: Azione|Commedia|Drama) -> str:
        if not isinstance(film, (Azione|Commedia|Drama)):
            raise ValueError("Film non valido")
        for f in self.film_list:
            if f.getId() == film.getId(): 
                print(f"Il film scelto è disponibile: '{film.getTitle()}'")
                return True
        print(f"Il film scelto non è disponibile: '{film.getTitle()}'")
        return False
            
    def rentAMovie(self, film: Azione|Commedia|Drama, client_id: int) -> None:
        if not isinstance(film, (Azione|Commedia|Drama)):
            raise ValueError("Film non valido")
        if not isinstance(client_id, int) or client_id <= 0:
            raise ValueError("Il codice cliente deve essere un numero intero positivo")
        if self.isAvailable(film):
            self.film_list.remove(film)
            if client_id not in self.rented_film:
                self.rented_film[client_id] = []
            self.rented_film[client_id].append(film)
            print(f"Il cliente {client_id} ha noleggiato {film.getTitle()}")
        else:
            print(f"Non è possibile noleggiare il film {film.getTitle()}")
    
    def giveBack(self, film: Azione|Commedia|Drama, client_id: int, days: int) -> None:
        if not isinstance(film, (Azione|Commedia|Drama)):
            raise ValueError("Film non valido")
        if not isinstance(client_id, int) or client_id <= 0:
            raise ValueError("Il codice cliente deve essere un numero intero positivo")
        if not isinstance(days, int) or days <= 0:
            raise ValueError("Il numero dei giorni deve essere un numero intero maggiore di 0")
        if client_id not in self.rented_film:
            print(f"Il cliente {client_id} non è presente nel dizionario")
            return
        if film in self.rented_film[client_id]:
            self.rented_film[client_id].remove(film)
            self.film_list.append(film)
            penale_da_pagare = film.calcolaPenaleRitardo(days)
            print(f"Cliente {client_id}! La penale da pagare per il film {film.getTitle()} è di {penale_da_pagare:.2f} euro!")
        else:
            print(f"Il film '{film.title} non è presente nella lista del cliente {client_id}")
                              
    def printMovies(self) -> str:
        if not self.film_list:
            print("Nessun film disponibile in negozio")
            return
        for film in self.film_list:
            print(f"'{film.getTitle()}' - {film.getGenere()}")

    def printRentMovies(self, client_id: int) -> str:
        if client_id not in self.rented_film or not self.rented_film[client_id]:
            print("Codice cliente non valido o nessun film noleggiato!")
            return
        else:
            for film in self.rented_film[client_id]:
                print(film)
        


         
