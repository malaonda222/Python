class Movie:
    def __init__(self, movie_id: str, title: str, director: str) -> None:
        self.movie_id = movie_id
        self.title = title 
        self.director = director 
        self.is_rented = False 
    
    def rent(self) -> None:
        if self.is_rented:
            raise ValueError(f"Il film {self.title} è già noleggiato.")
        else:
            self.is_rented = True 
    
    def return_movie(self) -> None:
        if not self.is_rented:
            raise ValueError(f"Il film {self.title} non è stato noleggiato da questo cliente.")
        else:
            self.is_rented = False

class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id = customer_id
        self.name = name 
        self.rented_movies: list[Movie] = []

    def rent_movie(self, movie: Movie) -> None:
        if movie.is_rented:
            print("Il film è già stato noleggiato.")
        else:
            self.rented_movies.append(movie)
            movie.rent()
    
    def return_movie(self, movie: Movie) -> None:
        if movie in self.rented_movies:
            movie.return_movie()
            self.rented_movies.remove(movie)
        else:
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente.")
    

class VideoRentalStore:
    def __init__(self) -> None:
        self.movies: dict[str, Movie] = {}
        self.customers: dict[str, Customer] = {}
    
    def add_movie(self, movie_id: str, title: str, director: str) -> None:
        if movie_id in self.movies:
            print(f"Il film con ID {movie_id} esiste già.")
        else:
            movie = Movie(movie_id, title, director)
            self.movies[movie_id] = movie

    def register_cutomer(self, customer_id: str, name: str) -> None:
        if customer_id in self.movies:
            print(f"Il cliente con ID {customer_id} è già registrato.")
        else:
            customer = Customer(customer_id, name)
            self.customers[customer_id] = customer 
    
    def rent_movie(self, customer_id, movie_id: str) -> None:
        if customer_id in self.customers and movie_id in self.movies:
            movie: Movie = self.movies[movie_id]
            self.customers[customer_id].rent_movie(movie)
        else:
            print(f"Cliente o film non trovato nel videonoleggio.")

    def return_movie(self, customer_id: str, movie_id: str) -> None:
        if customer_id not in self.customers and movie_id not in self.movies:
            print("Cliente o film non trovato nel videonoleggio.")
        else:
            movie: Movie = self.movies[movie_id]
            self.customers[customer_id].return_movie(movie)
    
    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        if customer_id not in self.customers:
            print("Cliente non trovato.")
            return []
        else:
            return self.customers[customer_id].rented_movies