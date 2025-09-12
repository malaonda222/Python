class MovieCatalog:
    def __init__(self) -> None:
        self.catalogo = {}

    def add_movie(self, director_name: str, movies: list) -> str:
        if director_name in self.catalogo:
            for movie in movies:
                if movie not in self.catalogo[director_name]:
                    self.catalogo[director_name].append(movie)
                    print(f"Regista '{director_name} e i suoi film inseriti")
        else:
            self.catalogo[director_name] = list(movies)
        print(f"Film aggiunti alla lista di '{director_name}'")
        
    def remove_movie(self, director_name: str, movie_name: str, remove_director = True) -> str:
        self.director_name = director_name
        self.movie_name = movie_name
        if director_name in self.catalogo:
            if movie_name in self.catalogo[director_name]:
                self.catalogo[director_name].remove(movie_name)
                print(f"Il film '{movie_name}' del regista '{director_name}' è stato rimosso")
                if not self.catalogo[director_name] and remove_director:
                    del self.catalogo[director_name]
                    print(f"Il regista '{director_name}' è stato eliminato dal catalogo")
            else:
                print(f"Il film '{movie_name}' non è presente nel catalogo.")
        else:
            print(f"Il regista '{director_name}' non è presente nel catalogo.")
        
        
        
        if director_name not in self.catalogo:
            print(f"Il regista '{director_name}' non è presente nel catalogo")

        if movie_name not in self.catalogo[director_name]:
            print(f"Il film '{movie_name} non è presente nella lista del regista '{director_name}'")
        self.catalogo[director_name].remove(movie_name)

        if not self.catalogo[director_name]:
            del self.catalogo[director_name]
            print(f"Il film '{movie_name}' è stato rimosso. Il regista '{director_name}' è stato rimosso perché non ha più film")
        print(f"Il film '{movie_name}' è stato rimosso dalla lista di '{director_name}'")
    
    def list_directors(self) -> list:
        if not self.catalogo:
            print("Il catalogo è vuoto")
        else:
            lista_registi = list(self.catalogo.keys()) 
            print(f"La lista dei registi: " + ",".join(lista_registi))
        
    def get_movies_by_director(self, director_name: str) -> list | None | str:
        if director_name not in self.catalogo:
            print(f"Il regista '{director_name}' non è presente nel catalogo")
        print(self.catalog[director_name])
    
    def search_movies_by_title(self, title: str) -> list | str:
        risultato = {}
        for regista, movies in self.catalog.items():
            trovati = []
            for movie in movies:
                if title.lower() in movie.lower():
                    trovati.append(movie)
            if trovati:
                risultato[regista] = trovati
        if not risultato:
            print(f"Nessun film trovato con la parola '{title}' nel titolo")
        print(risultato)
    

catalogo = MovieCatalog()
print(catalogo.add_movie("Tarantino", ["Kill Bill", "Django"]))
print(catalogo.add_movie("Sorrentino", "Partenope"))
print(catalogo.add_movie("Spielberg", "Jurassik Park"))
print(catalogo.add_movie("Spielberg", "Lo Squalo"))

