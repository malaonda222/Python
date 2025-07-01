class Movie:
    def __init__(self, movie_id: str, title: str, director: str) -> None:
        self.movie_id = movie_id
        self.title = title 
        self.director = director  
        self.is_rented = False 

    def __str__(self) -> str:
        return f"Id film: {self.movie_id}\nTitolo: {self.title}\nDirettore: {self.director}\nPrestato: {self.is_rented}\n"
        
    def rent(self) -> None:
        '''Contrassegna il film come noleggiato se non è già noleggiato'''
        if not self.is_rented: 
            self.is_rented = True
        else:
            raise ValueError(f"Il film \"{self.title}\" è già stato noleggiato.")
    
    def return_movie(self) -> None:
        '''Contrassegna il film come restituito'''
        if self.is_rented:
            self.is_rented = False
        else:
            raise ValueError(f"Il film \"{self.title}\" non è stato noleggiato da questo cliente.")

class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id = customer_id
        self.name = name 
        self.rented_movies: list[Movie] = []

    def __str__(self) -> str:
        return f"Id customer: {self.customer_id}\nNome: {self.name}\nRented Movies:{self.rented_movies}\n"

    def rent_movie(self, movie: Movie) -> None:
        '''Aggiunge il film nella lista rented_movies se non è già stato noleggiato'''
        if not movie.is_rented:
            movie.is_rented = True
            self.rented_movies.append(movie)
        else:
            raise ValueError(f"Il film {movie.title} è già stato noleggiato.")
    
    def return_movie(self, movie: Movie) -> None:
        '''Rimuove il film dalla lista rented_movies se già presente'''
        if movie in self.rented_movies:
            movie.is_rented = False
            self.rented_movies.remove(movie)
        else:
            raise ValueError(f"Il film {movie.title} non è stato noleggiato da questo cliente.")

class VideoRentalStore:
    def __init__(self, customers: dict[str, Customer] = None, movies: dict[str, Movie] = None) -> None:
        self.customers: dict[str, Customer] = customers if customers is not None else {}
        self.movies: dict[str, Movie] = movies if movies is not None else {}
       
    
    def add_movie(self, movie_id: str, title: str, director: str) -> dict:
        '''Aggiunge un nuovo film nel videonoleggio se non è già presente'''
        if movie_id not in self.movies:
            self.movies[movie_id] = Movie(movie_id, title, director)
        else:
            raise ValueError(f"Il film con ID '{movie_id}' esiste già.")
        
    def register_customer(self, customer_id: str, name: str) -> dict:
        '''Iscrive un nuovo cliente nel videonoleggio se non è già presente'''
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(customer_id, name)
        else:
            raise ValueError(f"Il cliente con ID '{customer_id}' è già registrato.")
    
    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        '''Permette al cliente di noleggiare un film se entrambi esistono nel videonoleggio'''
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            if movie.is_rented:
                raise ValueError("Film è già noleggiato.")
            movie.is_rented = True
            customer.rent_movie(movie)
        else:
            raise ValueError(f"Cliente o film non trovato.")
        

    def return_movie(self, customer_id: str, movie_id: str) -> None:
        '''Permette al cliente di restituire un film se entrambi esistono nel videonoleggio''' 
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            if movie in self.rented_movies:
                movie.is_rented = False
                customer.return_movie(movie)
            else:
                raise ValueError(f"Film non è stato noleggiato dal cliente.")
        else:
            raise ValueError("Cliente o film non trovato")
    
    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        '''Restituisce la lista dei film noleggiati dal client'''
        if not customer_id:
            raise ValueError("Il customer_id non è valido.")
        if customer_id not in self.customers:
            raise ValueError("Cliente non trovato.")
        else:
            for movie in self.customers[customer_id].rented_movies:
                print(movie.title)


if __name__ == "__main__":
    film1 = Movie("145236", "Parasite", "Bong Joon Ho")
    film2 = Movie("898562", "Oblivion", "Kosinski")
    film3 = Movie("46952544", "Brimstone", "Koolhoven")
    print(film1)
    print(film2)
    print(film3)
film1.rent()
film2.rent()
print(film1)
print(film2)
film2.return_movie()
print(film2)

customer1 = Customer("54865", "Gianni")
print(customer1)
customer2 = Customer("5963565", "Piero")
print(customer2)
customer1.rent_movie(film2)
customer2.rent_movie(film3)
customer2.return_movie(film3)

noleggio = VideoRentalStore()
noleggio.register_customer("54865", "Gianni")
noleggio.register_customer("5963565", "Piero")
noleggio.add_movie("145236", "Parasite", "Bong Joon Ho")
noleggio.add_movie("898562", "Oblivion", "Kosinski")
noleggio.rent_movie("54865", "145236")
noleggio.rent_movie("5963565", "898562")
noleggio.get_rented_movies("54865")
noleggio.get_rented_movies("5963565")

