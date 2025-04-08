class Libro:
    def __init__(self, title:str, author:str, year:int):
        self.title = title
        self.author = author
        self.year = year

    def dettagli(self):
        print(f"Le informazioni del libro sono le seguenti:\n{self.title}, {self.author}, {self.year}.")
    
    def aggiorna_anno(self, nuovo_anno):
        self.year = nuovo_anno
        print(f"L'anno di pubblicazione è stato aggiornato: {self.year}")


libro1 = Libro("Tre Piani", "Nevo", 2022)
libro1.aggiorna_anno(2024)
libro1.dettagli()
libro2 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954)

class Cercatore:
    def __init__ (self, nome:str):
        self.nome = nome 
        self.biblioteca = []
    
    def cerca_libro(self, title:str):
        for libro in self.biblioteca:
            if libro.title == title:
                return f"Il libro {title} è stato trovato."
        return f"Il titolo {title} non è stato trovato."
    
    def aggiungi_libro(self, libro:str):
        self.biblioteca.append(libro)
        print(f"Il libro {libro.title} è stato aggiunto alla biblioteca.")

cercatore = Cercatore()
cercatore.aggiungi_libro(libro1)
cercatore.aggiungi_libro(libro2)

print(cercatore.cerca_libro("Tre Piani"))
print(cercatore.cerca_libro("Il Signore degli Anelli"))



