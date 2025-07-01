#dal modulo CatalogoFilm importare la classe MovieCatalog
from CatalogoFilm import MovieCatalog

#inizializzare un catalogo, ovvero un oggetto della classe MovieCatalog
catalog: MovieCatalog = MovieCatalog()

# print(catalog)

catalog.add_movies("Steven Spielberg", ["Casper", "Ritorno al Futuro"])

catalog.add_movies("Steven Spielberg", ["ET"])

catalog.add_movies("Quentin Tarantino", ["Pulp Fiction", "Kill Bill"])

catalog.remove_movie("Quentin Tarantino", "Kill Bill")

catalog.remove_movie("Quentin Tarantino", "Pulp Fiction")

print(catalog)

print(catalog.list_directors())

print(catalog.get_movies_by_director("Tim Burton"))

print(catalog.get_movies_by_director("Steven Spielberg"))

