class Libro:
    def __init__(self, titolo:str, autore:str):
        self.titolo = titolo
        self.autore = autore
        self.prestato = False

    def __str__(self):
        stato_libro = "Prestato" if self.prestato else "Disponibile"
        return f"{self.titolo}, {self.autore}: {stato_libro}"

class Biblioteca: 
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro:Libro) -> None:
        self.catalogo.append(libro)
        return f"Libro {self.titolo} è stato aggiunto al catalogo."
        
    def presta_libro(self, titolo:str) -> None:
        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower():
                if libro.prestato:
                    return "Il libro {titolo} è già stato prestato."
                else:
                    libro.prestato = True
                    return "Il libro {titolo} è disponibile per il prestito."
        return f"Libro {titolo} non trovato nel catalogo."
  
    def restituisci_libro(self, titolo:str) -> None:
        for libro in self.catalogo:
            if libro.titolo.lower() == titolo.lower() and libro.prestato == True:
                libro.prestato = False 
                return f"Il libro {titolo} è stato restituito."
            else:
                return f"Il libro {titolo} non era stato prestato."
        return f"Il libro {titolo} non è stato trovato nel catalogo."

    def mostra_libri_disponibili(self) -> None:
        libri_disponibili = []
        for libro in self.catalogo:
            if libro.prestato == False:
                libri_disponibili.append(libro.titolo)

        if libri_disponibili: 
            return libri_disponibili
        else:
            return "Nessun libro è disponibile."
        
