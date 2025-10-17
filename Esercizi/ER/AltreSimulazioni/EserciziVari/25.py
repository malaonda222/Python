'''Descrizione:
Scrivi una funzione chiamata get_adults_names che riceve in ingresso una lista di dizionari.
Ogni dizionario rappresenta una persona e contiene le chiavi "nome" e "eta".
 
La funzione deve restituire una lista con solo i nomi delle persone la cui età 
è maggiore o uguale a 18.'''

def get_adults_names(people: list[dict[str, str|int]]) -> list[str]:
    nuova_lista = []
    for person in people:
        nome = person["nome"]
        eta = person["eta"]
        if eta >= 18:
            nuova_lista.append(nome)
    return nuova_lista


def get_adults_names1(people: list[dict[str, str|int]]) -> list[str]:
    return [person["nome"] for person in people if person["eta"] >= 18]


print(get_adults_names([
    {"nome": "Sara", "eta": 21},
    {"nome": "Luca", "eta": 16}
]))

print(get_adults_names1([
    {"nome": "Sara", "eta": 21},
    {"nome": "Luca", "eta": 16}
]))
