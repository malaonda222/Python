'''
Nome dell’esercizio: filter_and_format_people
Traccia:
Scrivi una funzione chiamata filter_and_format_people che prende in input:
* people: lista di dizionari con chiavi "nome" (str) e "età" (int)
* min_age: intero

La funzione deve:
* Filtrare tutte le persone la cui età è maggiore o uguale a min_age.
* Convertire ogni persona filtrata in una stringa nel formato "nome(età)".
* Restituire una stringa unica con tutte le persone filtrate concatenate, separate da una virgola ",".
'''

def filter_and_format_people(people: list[dict[str, int]], min_age: int) -> str:
    nuova_lista = []
    for person in people:
        eta = person["eta"]
        nome = person["nome"]
        if eta >= min_age:
            formattato = f"{nome}({eta})"
            nuova_lista.append(formattato)
    return ",".join(nuova_lista)

print(filter_and_format_people([{"nome": "Lisa", "eta": 22},
                                {"nome": "Luigi", "eta": 18},
                                {"nome": "Elena", "eta": 15}], 18))