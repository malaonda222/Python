'''Esercizio 1: Creazione e stampa di un dizionario
Crea un dizionario che contenga le informazioni di un libro (titolo, autore, anno di pubblicazione). 
Stampa il dizionario.
Obiettivo:
    Creare un dizionario con chiavi titolo, autore e anno.
    Stampare il dizionario.'''

def crea_diz(titolo: str, autore: str, anno: int) -> dict:
    dizionario: dict = {
        "titolo": titolo,
        "autore": autore,
        "anno": anno
    }
    return dizionario

print(crea_diz(titolo="Tre Piani", autore="Nevo", anno=2005))