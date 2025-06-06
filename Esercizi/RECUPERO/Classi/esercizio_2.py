class Movie:
    def __init__(self, movie_id: str, title: str, director: str):
        self.movie_id = movie_id
        self.title = title 
        self.director = director  
        self.is_rented = False 

    def __str__(self):
        return f"Id film: {self.movie_id}\nTitolo: {self.title}\nDirettore:{self.director}\nPrestato: {self.is_rented}"
        
    def rent(self):
        '''Contrassegna il film come noleggiato se non è già noleggiato'''
        if not self.is_rented: 
            self.is_rented = True
        else:
            print(f"Il film \"{self.title}\" è già stato noleggiato.")
    
    def return_movie(self):
        '''Contrassegna il film come restituito'''
        if not self.is_rented:
            print(f"Il film \"{self.title}\" non è stato noleggiato da questo cliente.")
        else:
            self.is_rented = False 
            print(f"Il film \"{self.title}\" è stato restituito con successo.")

class Customer:
    def __init__(self, customer_id: str, name: str, rented_movies: list[Movie] = None):
        self.customer_id = customer_id
        self.name = name 
        if rented_movies is None:
            rented_movies = []
        self.rented_movies = rented_movies

    def rent_movie(self, movie: Movie):
        if not movie.is_rented:
            movie.is_rented = True
            self.rented_movies.append(movie)
        else:
            print(f"Il film {movie.title} è già stato noleggiato.")
    
    def return_movie(self, movie: Movie):
        if movie in self.rented_movies:
            movie.is_rented = False
            self.rented_movies.remove(movie)
        else:
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente.")

class VideoRentalStore:
    def __init__(self):
        self.movies: dict[str[Movie]] = {}
        self.customers: dict[str, Customer] = {}
    
    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id not in self.movies:
            self.movies[movie_id] = Movie(movie_id, title, director)
        else:
            raise ValueError(f"Il film con ID '{movie_id}' esiste già.")
        
    def register_customer(self, customer_id: str, name: str):
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(customer_id, name)
        else:
            raise ValueError(f"Il cliente con ID '{customer_id}' è già registrato.")
    
    def rent_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.rent_movie(movie)
            print(f"Film {movie_id} noleggiato dal cliente {customer_id}.")
        else:
            raise ValueError("Cliente o film non trovato.")

    def return_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.return_movie(movie)
            print(f"Film {movie_id} restituito dal cliente {customer_id}")
        else:
            raise ValueError("Cliente o film non trovato")
    
    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        if customer_id in self.customers    :
            return self.customers[customer_id].rented_movies
        else:
            print("Cliente non trovato")
            return list()
            
            