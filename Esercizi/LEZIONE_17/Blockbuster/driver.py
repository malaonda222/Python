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
blockbuster.rentAMovie("Kill Bill", 456)
blockbuster.rentAMovie("Top Gun", 456)
blockbuster.rentAMovie("Top Gun", 698)
blockbuster.rentAMovie("Tre uomini e una gamba", 698)
blockbuster.giveBack("Top Gun", 456, 3)
blockbuster.printMovies()