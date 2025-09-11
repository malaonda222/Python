class Libro:
    def __init__(self, titolo: str, autore: str, prestato: bool = False) -> None:
        self.titolo = titolo
        self.autore = autore 
        self.prestato = prestato 
    
    def __str__(self) -> str:
        return f"Titolo: {self.titolo}\nAutore: {self.autore}\nPrestato: {self.prestato}"

class Biblioteca:
    def __init__(self) -> None:
        self.catalogo = [] 
    
    def aggiungi_libro(self, libro: Libro) -> str:
        self.catalogo.append(libro)
        return f"'{libro.titolo}' aggiunto al catalogo"
    
    def presta_libro(self, titolo: str) -> str:
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if not libro.prestato:
                    libro.prestato = True
                    return f"Il libro '{titolo}' è stato prestato"
                else:
                    return f"Il libro '{titolo}' non è disponibile per il prestito"
            else:
                return f"Il libro '{titolo}' non è presente nel catalogo"
            
    def restituisci_libro(self, titolo: str) -> str:
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if libro.prestato:
                    libro.prestato = False 
                    return f"Il libro '{titolo}' è stato restituito"
                else:
                    return f"Il libro '{titolo}' non risultato essere stato prestato"
            else:
                return f"Il libro '{titolo}' non è presente nel catalogo"
            
    def mostra_libri_disponibili(self) -> list | None:
        if not self.catalogo:
            return "Non ci sono libri nel catalogo"
        else:
            libri_disponibili = []
            for libro in self.catalogo:
                if libro.prestato == False:
                    libri_disponibili.append(libro)
            
            if not libri_disponibili:
                return f"Non ci sono libri disponibili al momento"
            return "Lista dei libri disponibili:\n" + "\n".join([str(libro) for libro in libri_disponibili])

        

libro1 = Libro("Mille Notti", "Rinaldi")
print(libro1)
libro2 = Libro("La Divina Commedia", "Alighieri")
print(libro2)
libro3 = Libro("I Promessi Sposi", "Manzoni")
print(libro3)
print()
biblioteca = Biblioteca()
print(biblioteca.aggiungi_libro(libro1))
print(biblioteca.aggiungi_libro(libro2))
print(biblioteca.aggiungi_libro(libro3))
print(biblioteca.presta_libro("Mille Notti"))
print(biblioteca.mostra_libri_disponibili())

