class Libro:
    def __init__(self, titolo:str, autore:str, copie:int):
        self.titolo = titolo
        self.autore = autore
        self.copie = copie 
    
    def __str__(self):
        return f"Il libro si intitola \"{self.titolo}\", scritto da {self.autore}, copie disponibili {self.copie}."
    

class Biblioteca:
    def __init__(self):
        self.catalogo = []
    
    def aggiungi_libro(self, libro:Libro):
        self.catalogo.append(libro)
        return f"Aggiunto libro {libro.titolo} di {libro.autore}."
    
    def presta_libro(self, titolo:str):
        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower():
                libro.copie -= 1 
                return f"Il libro \"{libro.titolo}\" adesso è in stato \"Prestito\"."
            else:
                return f"Il libro \"{libro.titolo}\" non è disponibile al momento."
        else:
            return f"Il libro \"{titolo}\" non è presente nel catalogo."

    def restituisci_libro(self, titolo:str):
        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower():
                libro.copie += 1
                print(f"Hai restituito il libro {libro.titolo}.")
                return 
        print("Libro non riconosciuto.")

    def mostra_catalogo(self):
        print("---Catalogo Biblioteca---")
        for libro in self.catalogo:
            print(f" - {libro}")

libro1 = Libro("Un giorno questo dolore ti sarà utile", "Cameron", 2)
libro2 = Libro("Tre Piani", "Nevo", 5)
print(libro1)
print(libro2)

biblio = Biblioteca()
biblio.aggiungi_libro(libro1)
biblio.aggiungi_libro(libro2) 

biblio.presta_libro("Tre Piani")
biblio.presta_libro("Tre Piani")
biblio.restituisci_libro("Tre Piani")
biblio.restituisci_libro("Cuore")
biblio.mostra_catalogo()