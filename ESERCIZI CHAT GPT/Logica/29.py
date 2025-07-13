'''Scrivi una funzione frequenza_lettere(testo: str) -> dict che:
    Prende una stringa in input (testo)
    Restituisce un dizionario in cui:
        Le chiavi sono le lettere dell’alfabeto presenti nella stringa (solo quelle)
        I valori sono il numero di volte che ciascuna lettera appare
    Ignora gli spazi, i numeri e i simboli
    Non fa distinzione tra maiuscole e minuscole'''

def frequenza_lettera(testo: str) -> dict:
    new_dict = {}
    testo = testo.lower()

    for element in testo:
        if element == " " or element.isdigit() or not element.isalpha():
            continue 
        else:
            if element not in new_dict:
                new_dict[element] = 1 
            else:
                new_dict[element] += 1 
    return new_dict

print(frequenza_lettera("cia777%oooa"))
