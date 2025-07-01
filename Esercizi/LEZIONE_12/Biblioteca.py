class Libro:
    def __init__(self, titolo: str, autore: str):
        self._titolo = titolo 
        self._autore = autore 
        self._non_prestato = True

    def setTitolo(self, titolo: str) -> None:
        if not isinstance(titolo, str) or titolo.strip() == "":
            raise ValueError("Errore. Il titolo deve essere una stringa e non può essere vuoto")
        else:
            self._titolo = titolo
        
    def setAutore(self, autore: str) -> None:
        if not isinstance(autore, str) or autore.strip() == "":
            raise ValueError("Errore. L'autore deve essere una stringa e non può essere vuota.")
        else:
            self._autore = autore

    def getTitolo(self) -> str:
        return self._titolo
    
    def getAutore(self) -> str:
        return self._autore

    def __str__(self):
        stato_libro: str = "Prestato" if self._non_prestato else "Disponibile"
        return f"Titolo: {self.getTitolo()}\nAutore: {self.getAutore()}\nStato: {stato_libro}"
    
class Biblioteca:
    def __init__(self):
        self.catalogo = list()

    def aggiungi_libro(self, libro: str) -> None:
        self.catalogo.append(libro)
        print(f"Libro \"{libro.getTitolo()}\" è stato aggiunto al catalogo.")

    def presta_libro(self, titolo: str) -> None:
        for libro in self.catalogo:
            if libro._titolo.lower() == titolo.lower():
                if libro._non_prestato:
                    print(f"Il libro \"{titolo}\" è stato preso in prestito.")
            else:
                self._non_prestato = True 
                print(f"Il libro \"{titolo}\" non è diponibile al momento. ")
        else:
            print(f"Il libro \"{titolo}\" non è presente nel catalogo.")

    def restituisci_libro(self, titolo: str) -> None:
        for libro in self.catalogo:
            if libro._titolo.lower() == titolo.lower():
                if libro._non_prestato:
                    libro._non_prestato = False 
                    print(f"Il libro \"{titolo}\" è stato restituito ed è di nuovo disponibile.")
                else:
                    print(f"Il libro \"{titolo} è disponibile per il prestito.")
        else:
            print(f"Il libro \"{titolo}\" non è presente nel catalogo.")

    def mostra_libri_disponibili(self):
        libri_disponibili = [str(libro) for libro in self.catalogo if not libro._non_prestato]
        if not self.catalogo:
            print("Il catalogo dei libri è vuoto.")
        else:
            print("Libri disponibili:\n")
            for libro in libri_disponibili:
                print(f"- {libro}")

    def mostra_stato_libri(self) -> None:
        for libro in self.catalogo:
            print(f" - {libro}")

libro1 = Libro("La coscienza di Zeno", "Italo Svevo")
libro2 = Libro("Don Chisciotte", "Miguel de Cervantes")
libro3 = Libro("Divina Commedia", "Dante Alighieri")

catalogue = Biblioteca()
catalogue.aggiungi_libro(libro1)
catalogue.aggiungi_libro(libro2)
# catalogue.aggiungi_libro(libro3)
catalogue.presta_libro("La coscienza di Zeno")
catalogue.presta_libro("Tre Piani")
catalogue.mostra_libri_disponibili()
catalogue.mostra_stato_libri()
