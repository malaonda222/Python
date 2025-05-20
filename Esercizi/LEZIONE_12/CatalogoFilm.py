class MovieCatalog:
    '''
    Attributi della classe MovieCatalog
    self.catalog: dict[str, list[str]]
    '''
    #inizializzare degli oggetti della classe MovieCatalogue
    def __init__(self) -> None: #non si è obbligati a mettere parametri
        self.setCatalog()

    #metodo getter che ritorna il valore dell'attributo self.catalog
    def getCatalog(self) -> dict[str, list[str]]:
        return self.catalog 
    
    #metodo settere che consente di inzializzare l'attributo self.catalog
    def setCatalog(self) -> None:
        self.catalog: dict[str, list[str]] = {}
    
    #metodo per visualizzare dettagli del catalogo 
    def __str__(self) -> str:
        string: str = "Catalogo:"
        if self.catalog:
            for key, values in self.catalog.items():
                temp_string:str = "\n" + str(key) + ": " + str(values)
                string = string + temp_string
        return string 
    
    #oppure si usa return str(self.catalog)
    

    #metodi della classe MovieCatalog

    #metodo che aggiunge una lista di film di uno specifico regista al catalogo
    def add_movies(self, director_name: str, movies: list[str]) -> None:
        #check se il regista non è valido 
        if not director_name:
            print(f"Il regista non è valido.")
        #check se la lista di film non è valida 
        elif not movies:
            print(f"La lista dei film non può essere vuota.")
        #se i dati sono validi
        else:
            #se il regista è presente nel catalogo
            if director_name in self.catalog:
                #aggiungere la lista movies al catalogo
                #per ogni film nella lista movies
                for movie in movies:
                    #controllare se il film è già stato aggiunto al catalogo
                   
                    #dizionario[key] -> valore
                    #director_name è la chiave del dizionario che rappresenta il nome di un regista
                    #a questa chiave corrisponde una lista di film, ovvero i film prodotti dal regista in questione
                    #self.catalog[director_name] = è il valore associato alla chiave di director_name
                    # -> ovvero è la lista di tutti i film prodotti dal regista 
                    if movie in self.catalog[director_name]:
                        print(f"Il film {movie} è già presente nel catalogo.")
                    
                    #se il film non è presente
                    else:
                        #aggiungere il film al catalogo 
                        self.catalog[director_name].append(movie)
            
            #se il regista non è presente nel catalogo
            else:
                #creare un nuovo record
                self.catalog[director_name] = movies 

    def remove_movie(self, director_name: str, movie: str) -> None:
        if not director_name:
            print(f"Il regista non è valido.")
        #check se la lista di film non è valida 
        elif not movie:
            print(f"Il film non è valido.")
        #se i dati sono validi
        else:
            #se il regista è presente nel catalogo e, in caso, controllare se il film movie è nella 
            #lista dei film prodotti dal regista in questione
            if director_name in self.catalog and movie in self.catalog[director_name]:
                #rimuovere il film dalla lista
                self.catalog[director_name].remove(movie)
            #verificare se la lista dei film è vuota
            if not self.catalog[director_name]:
            #(selfcatalog dizionario, director name è la chiave e movie è la lista dei film quindi valore)
                #rimuovere la lista se la lista è vuota
                del self.catalog[director_name]

    #metodo che ritorna una lista contenente i nomi di tutti i registi del catalogo
    def list_directors(self) -> list[str] | str:
        #controllare se il dizionario self.catalog non è vuoto
        if self.catalog:
            return list(self.catalog.keys())
        #se dizionario è vuoto
        else:
            return(f"Non ci sono registi nel catalogo perché il catalogo è vuoto.")
        
    #metodo che dato un regista restituisca tutti i film da esso prodotti
    def get_movies_by_director(self, director_name) -> list[str] | str:
        if not director_name:
            print("Il regista non è valido.")
        #se valido
        else:
            #controllo se regista è nel catalogo
            if director_name in self.catalog:
                return self.catalog[director_name]
            #se il regista non è nel catalogo
            else:
                return f"Il regista {director_name} non si trova nel catalogo!"
            
    #metodo che dato un titolo restituisca tutti i film che contengono una certa parola nel titolo
    