'''
Tema: Dizionari - Raggruppamento di dati
Obiettivo: Costruire un dizionario a partire da una lista, 
organizzando gli elementi secondo una logica specifica.
 
Nome dell’esercizio: Raggruppa parole per lunghezza
 
Traccia:
Scrivi una funzione raggruppa_parole(parole: list[str]) -> dict[int, list[str]] che, 
dato un elenco di parole, le raggruppi in un dizionario in base alla loro lunghezza.
 
La chiave del dizionario deve essere la lunghezza della parola, e il valore deve essere 
la lista delle parole di quella lunghezza.
 
Esempio input:
parole = ["cane", "gatto", "sole", "luna", "amico", "io", "tu", "computer"]
 
Suggerimento:
Puoi scorrere la lista parola per parola, calcolare la lunghezza e inserire la parola 
nella lista corrispondente nel dizionario. Se la chiave non esiste ancora, devi crearla.
'''


def raggruppa_parole(parole:list[str]) -> dict[int, list[str]]:
    new_dict = {}
    for parola in parole: 
        lunghezza = len(parola)
        if lunghezza in new_dict:
            new_dict[lunghezza] += [parola] 
        else:
            new_dict[lunghezza] = [parola] 
    return new_dict

parole = ["cane", "gatto", "sole", "luna", "amico", "io", "tu", "computer"]
print(raggruppa_parole(parole))