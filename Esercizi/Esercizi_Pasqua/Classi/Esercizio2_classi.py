class MovieCatalog:
    def __init__(self):
        self.catalogo = {}

    def add_movie(self, director_name: str, movies:list[str]):
        if director_name in self.catalogo:
            for movie in movies:
                if movie not in self.catalogo[director_name]:
                    self.catalogo[director_name].append(movie)
        else:
            self.catalogo[director_name] = list(movies)
        print(f"Film aggiunti al regista {director_name}.")
    
    def remove_movie(self, director_name:str, movie_name: str, remove_director=True):
        self.director_name = director_name
        self.movie_name = movie_name
        if director_name in self.catalogo:
            if movie_name in self.catalogo[director_name]:
                self.catalogo[director_name].remove(movie_name)
                print(f"Il film {movie_name} del regista {director_name} è stato rimosso.")
                if not self.catalogo[director_name] and remove_director:
                    del self.catalogo[director_name] 
                    print(f"Il regista {director_name} è stato eliminato dal catalogo.")
            else: 
                print(f"Il film {movie_name} non è presente nella lista dei film del regista {director_name}.")
        else:
            print(f"Il regista {director_name} non è presente nel catalogo.")
    
    def list_directors(self):
        if self.catalogo:
            print(f"I registi presenti nel catalogo:")
            for director in self.catalogo:
                print(f"- {director}")
        else:
            print("Non c'è nessun regista presente nel catalogo.")
    
    def get_movies_by_director(self, director_name:str):
        if director_name in self.catalogo:
            print(self.catalogo[director_name])
        print(f"Il regista {director_name} non è presente nel catalogo.")
    
    def search_movies_by_title(self, title:str):
        match = {}
        for director_name, movies in self.catalogo.items():
            matched_movies = []
            for movie in movies:
                if title.lower() in movie.lower():
                    matched_movies.append(movie)
            if matched_movies:
                match[director_name] = matched_movies
        if match:
            print(match)
        else:  
            print(f"Errore. Non è stato trovato nessun film con la parola {title}.")
        

catalogo = MovieCatalog()
catalogo.add_movie("Tarantino", ["Pulp Fiction", "Bastardi senza gloria", "Kill Bill"])
catalogo.add_movie("Steven Spielberg", ["Jurassic Park", "Jaws", "Schindlers List"])  
catalogo.add_movie("Tarantino", "Django")
catalogo.add_movie("Steven Spielberg", "The Fabelmans")
catalogo.remove_movie("Tarantino", "Pulp Fiction")
catalogo.remove_movie("Steven Spielberg", "Jaws")

catalogo.list_directors()

catalogo.get_movies_by_director("Steven Spielberg")

catalogo.search_movies_by_title("Park")


        
    
    
