'''Esercizio: Rimuovere le vocali da una stringa
Obiettivo:
Scrivi una funzione che prenda una stringa come input e restituisca una nuova stringa senza 
le vocali (a, e, i, o, u e rispettivamente maiuscole A, E, I, O, U).

Indicazioni:
La stringa può contenere maiuscole, minuscole, numeri e simboli.
Rimuovi solo le vocali, mantenendo intatte le altre lettere e i caratteri non alfabetici.
'''

def rimuovi_vocali(stringa: str) -> str:
    vocali = 'aeiouAEIOU'
    nuova_lista = []

    if not stringa:
        return "Errore, lista vuota"

    for carattere in stringa:
        if carattere not in vocali:
            nuova_lista.append(carattere) 
        

    nuova_stringa_totale = "".join(nuova_lista)
    return nuova_stringa_totale

print(rimuovi_vocali("Ciao mi chiamo, Lisa?"))



def rimuovi_vocali1(stringa: str) -> str:
    vocali = "aeiouAEIOU"
    nuova_stringa = "".join([carattere for carattere in stringa if carattere not in vocali])
    return nuova_stringa