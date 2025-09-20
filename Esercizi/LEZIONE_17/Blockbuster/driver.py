from film import Film 
from movie_genre import Azione, Commedia, Drama 
from noleggio import Noleggio 

lista_film = [
    Azione(265, "Kill Bill"),
    Azione(4268, "Top Gun"),
    Azione(30495, "Jumanji"),
    Azione(3628, "Django"),
    Azione(123, "Inception"),
    Commedia(2901, "Ciclone"),
    Commedia(46290, "Benvenuti al Sud"),
    Commedia(647, "Tre uomini e una gamba"),
    Commedia(2203, "Come un gatto in tangenziale"),
    Drama(678, "Schindlerslist")
]

blockbuster = Noleggio(lista_film)
print("Quale film vuoi noleggiare? ")

film1 = lista_film[0]
blockbuster.rentAMovie(film1, 456)

film2 = lista_film[1]
blockbuster.rentAMovie(film2, 456)

blockbuster.rentAMovie(film2, 698)

film3 = lista_film[7]
blockbuster.rentAMovie(film3, 698)

blockbuster.giveBack(film2, 456, 3)

print("Lista dei film disponibili: ")
blockbuster.printMovies()

blockbuster.printRentMovies(698)

