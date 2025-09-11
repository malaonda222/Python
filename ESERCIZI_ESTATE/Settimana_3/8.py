class MovieCatalog:
    def __init__(self) -> None:
        self.catalogo = {}

    def add_movie(self, director_name: str, movies: list) -> str:
        if director_name in self.catalogo:
            self.catalogo[director_name].extend(movies)
            return f"Film aggiunti alla lista di '{director_name}'"
        else:
            self.catalogo[director_name] = movies
            return f"Aggiunti il regista '{director_name}' e i suoi film"
        
    def remove_movie(self, director_name: str, movie_name: str) -> str:
        if director_name not in self.catalogo:
            return f"Il regista '{director_name}' non è presente nel catalogo"

        if movie_name not in self.catalogo[director_name]:
            return f"Il film '{movie_name} non è presente nella lista del regista '{director_name}'"
        self.catalogo[director_name].remove(movie_name)

        if not self.catalogo[director_name]:
            del self.catalogo[director_name]
            return f"Il film '{movie_name}' è stato rimosso. Il regista {director_name} è stato rimosso perché non ha più film"
        return f"Il film '{movie_name}' è stato rimosso dalla lista di {director_name}"
    
    def list_directors(self) -> list:
        if not self.catalogo:
            return "Il catalogo è vuoto"
        else:
            lista_registi = list(self.catalogo.keys()) 
            return f"La lista dei registi: " + ",".join(lista_registi)
        
    def get_movies_by_director(self, director_name: str) -> list | None | str:
        if director_name not in self.catalogo:
            return f"Il regista '{director_name}' non è presente nel catalogo"
        return self.catalog[director_name]
    
    def search_movies_by_title(self, title: str) -> list | str:
        risultato = []
        for regista, film_list in self.catalog.items():
            for film in film_list:
                if title.lower() in film.lower():
                    risultato.append({"regista": regista, "film": film})
        if not risultato:
            return f"Nessun film trovato con la parola '{title}' nel titolo"
        return risultato
    
