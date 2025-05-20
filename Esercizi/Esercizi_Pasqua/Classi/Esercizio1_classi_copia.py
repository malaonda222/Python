class Libro:
    def __init__(self, titolo: str, autore: str):
        self.titolo = titolo 
        self.autore = autore 
        self.prestato = False 
    
    def __str__(self):
        stato_libro = "Prestato" if self.prestato else "Disponibile"
        return f"Titolo: {self.titolo}\nAutore: {self.autore}\nStato del prestito: {stato_libro}"

class Biblioteca:

    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro: Libro) -> None:
        self.catalogo.append(libro)
        print(f"Libro \"{libro.titolo}\" aggiunto al catalogo.")

    def presta_libro(self, titolo: str) -> None:
        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower():
                if libro.prestato: 
                    print(f"Libro \"{titolo}\" disponibile e prestato.")
                else:
                    libro.prestato = True
                    print(f"Libro \"{titolo}\" disponibile per il prestito.")
                return 
        print(f"Il titolo del libro \"{titolo}\" non è presente nel catalogo.")

    def restituisci_libro(self, titolo: str) -> None:
        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower():
                if libro.prestato:
                    libro.prestato = False
                    print(f"Libro \"{titolo}\" restituito e di nuovo disponibile.")
                else:
                    print(f"Libro \"{titolo}\" disponibile per il prestito.")
                return
        print(f"Il libro \"{titolo}\" non è presente nel catalogo.")
    
    def mostra_libri_disponibili(self) -> None:
        libri_disponibili = [str(libro) for libro in self.catalogo if not libro.prestato]
        if not libri_disponibili:
            print("Nessun libro disponibile.")
        else:
            print("Libri disponibili: ")
            for libro in libri_disponibili:
                print(f"- {libro}")
    
    def mostra_stato_libri(self) -> None:
        print("Mostra stato attuale dei libri: ")
        for libro in self.catalogo:
            print(f" - {libro}")

libro1 = Libro("La coscienza di Zeno", "Italo Svevo")
libro2 = Libro("Don Chisciotte", "Miguel de Cervantes")
libro3 = Libro("Divina Commedia", "Dante Alighieri")

catalogue = Biblioteca()
catalogue.aggiungi_libro(libro1)
catalogue.aggiungi_libro(libro2)
catalogue.aggiungi_libro(libro3)
catalogue.presta_libro("La coscienza di Zeno")
catalogue.presta_libro("Tre Piani")
catalogue.mostra_libri_disponibili()
catalogue.mostra_stato_libri()
