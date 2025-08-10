'''Esercizio 2: Accesso ai valori di un dizionario
Crea un dizionario contenente informazioni su un film (titolo, regista, anno di uscita, durata). 
Scrivi un programma che:
    Mostri il titolo del film.
    Modifichi l'anno di uscita.
    Aggiunga una nuova chiave per la valutazione del film (ad esempio, 8/10).
Obiettivo:
    Imparare ad accedere ai valori di un dizionario tramite le chiavi.
    Modificare i valori e aggiungere nuove chiavi'''

def dizionario_film(titolo: str, regista: str, anno_uscita: int, durata_min: int) -> dict:
    dizio: dict = {
        "titolo": titolo,
        "regista": regista,
        "anno di uscita": anno_uscita,
        "durata minuti": durata_min
    }
    return dizio

def mostra_titolo(dizio: dict):
    return f"Il titolo del film è: {dizio['titolo']}"

def aggiungi_valutazione(dizionario: dict, voto: int):
    if voto > 10 or voto < 0:
        print("Il voto deve essere tra 0 e 10")
    else:
        dizionario["voto"] = voto 
        print(f"valutazione aggiornata a {voto}/10")
    return dizionario

film = dizionario_film("Inception", "Christopher Nolan", 2010, 148)
print(mostra_titolo(film))
print(aggiungi_valutazione(film, 8))

film1 = dizionario_film("Kill Bill", "Tarantino", 2003, 120)
print(mostra_titolo(film1))
print(aggiungi_valutazione(film1, 9))