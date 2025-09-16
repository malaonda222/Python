'''Partendo dalla tua classe Libreria (dell’esercizio 1), aggiungi un attributo chiamato 
clienti_serviti, con valore predefinito 0.
Crea un’istanza della classe e stampa il numero di clienti serviti.
Modifica direttamente il valore di clienti_serviti e stampalo di nuovo.
Aggiungi un metodo imposta_clienti_serviti() che consenta di impostare il valore.
Aggiungi un altro metodo incrementa_clienti_serviti() che aumenti il numero di clienti 
serviti di una certa quantità.
Chiama entrambi i metodi con valori di esempio e mostra i risultati.'''

class Libreria:
    def __init__(self, nome_libreria: str, genere_principale: str, clienti_serviti = 0) -> None:
        self.nome_libreria = nome_libreria
        self.genere_principale = genere_principale
        self.clienti_serviti = clienti_serviti
    
    def descrivi_libreria(self):
        print(f"Nome libreria: {self.nome_libreria} - Genere principale: {self.genere_principale} - Clienti serviti: {self.clienti_serviti}")

    def imposta_clienti_serviti(self, clienti_serviti: int):
        self.clienti_serviti = clienti_serviti
        print(f"Il numero di clienti serviti è stato aggiornato a: {self.clienti_serviti}")
    
    def incrementa_clienti_serviti(self, clienti_aggiunti: int):
        self.clienti_serviti += clienti_aggiunti
        print(f"I clienti adesso ammontano a: {self.clienti_serviti}")
    


libreria = Libreria("Leggendo", "Drammaturgia", 0)
libreria.descrivi_libreria()
libreria.imposta_clienti_serviti(12)
libreria.incrementa_clienti_serviti(10)
libreria.descrivi_libreria()



