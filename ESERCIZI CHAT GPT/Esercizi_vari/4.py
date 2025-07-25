'''
Traccia:
Ti viene fornita una lista di dizionari, dove ogni dizionario rappresenta uno studente 
con le seguenti chiavi:
 
* "nome": nome dello studente (stringa)
* "corso": il corso frequentato (stringa)
* "voto": il voto finale ottenuto (intero)
 
Scrivi una funzione che:
 
* Prenda in input questa lista.
* Filtri solo gli studenti che hanno voto maggiore o uguale a 18.
* Ritorni una nuova lista contenente solo i nomi degli studenti promossi.'''


def filtra_studente(lista1: list[dict]) -> list[str]:
    studenti_promossi = []
    for element in lista1:
        if element["voto"] >= 18:
            studenti_promossi.append(element["nome"])
    return studenti_promossi


print(filtra_studente([{"nome": "Lisa", "corso": "Matematica", "voto": 18}, 
                       {"nome": "Giulia", "corso": "Scienze", "voto": 15}]))
      
