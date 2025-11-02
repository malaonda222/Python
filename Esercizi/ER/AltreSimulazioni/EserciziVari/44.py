'''Esercizio: Contare la frequenza delle parole
Obiettivo:
Scrivi una funzione che prenda una stringa e restituisca un dizionario in cui le chiavi sono le parole uniche della stringa e i valori sono il numero di occorrenze di ciascuna parola.

Indicazioni:
La funzione deve essere case-insensitive, quindi "Ciao" e "ciao" devono essere considerati 
la stessa parola.
Ignora la punteggiatura (cioè "ciao!" deve essere considerato uguale a "ciao").
La stringa può contenere più parole, numeri, simboli e spazi.

Esempio:
Input: "Ciao, ciao! Come va? Ciao."
Output: {"ciao": 3, "come": 1, "va": 1}'''

import string 

def conta_frequenze(stringa: str) -> dict[str, int]:

    frequenze = {}
    if not stringa:
        return "Errore, stringa vuota"
    
    stringa = stringa.lower()
    stringa = stringa.translate(str.maketrans("", "", string.punctuation))
    parole = stringa.split()

    for parola in parole:
        if parola not in frequenze:
            frequenze[parola] = 1
        else:
            frequenze[parola] += 1
    
    return frequenze

print(conta_frequenze("Ciao, ciao! Come va? Ciao."))