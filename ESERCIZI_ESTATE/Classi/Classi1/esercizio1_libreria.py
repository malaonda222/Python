'''Crea una classe chiamata Libreria.
Il metodo __init__() deve memorizzare due attributi: nome_libreria e genere_principale.
Crea un metodo chiamato descrivi_libreria() che stampi queste due informazioni in modo 
leggibile.
Crea un altro metodo chiamato apri_libreria() che stampi un messaggio che indica che la 
libreria è aperta.
Crea un'istanza della classe e:
Stampa i due attributi separatamente.
Chiama entrambi i metodi.'''

class Libreria:
    def __init__(self, nome_libreria: str, genere_principale: str) -> None:
        self.nome_libreria = nome_libreria
        self.genere_principale = genere_principale
    
    def descrivi_libreria(self):
        print(f"Nome libreria: {self.nome_libreria} - Genere principale: {self.genere_principale}")

    def apri_libreria(self):
        print("La libreria è aperta!")


libreria = Libreria("Canova", "Narrativa")
libreria.descrivi_libreria()
libreria.apri_libreria()