'''
Tema: Liste e dizionari
Obiettivo: Separare elementi di tipi diversi presenti in una lista e organizzarli in un dizionario
 
Nome dell’esercizio: raggruppa_numeri_parole
 
Traccia:
Scrivi una funzione raggruppa_numeri_parole(lista: list) che, 
data una lista contenente numeri e parole, ritorni un dizionario con due chiavi:
"numeri" → lista contenente tutti gli elementi di tipo numerico presenti nella lista
"parole" → lista contenente tutti gli elementi di tipo stringa presenti nella lista
 
Esempio:
input: [1, "ciao", 3, "python", 7]
output: {"numeri": [1, 3, 7], "parole": ["ciao", "python"]}
 
Suggerimento:
Puoi usare un ciclo for per scorrere la lista e la funzione isinstance() per distinguere numeri e stringhe.
'''

def raggruppa_numeri_parole(lista: list[str|int]) -> dict[str, str]:
    lista_numeri = []
    lista_parole = []
    for element in lista:
        if isinstance(element, int):
            lista_numeri.append(element)
        if isinstance(element, str):
            lista_parole.append(element)
    return {"numeri": lista_numeri, "parole": lista_parole}


def raggruppa_numeri_parole2(lista: list[str|int]) -> dict[str, str]:
    new_dict = {"numeri": [], "parole": []}
    for element in lista:
        if isinstance(element, int):
            new_dict["numeri"].append(element)
        if isinstance(element, str):
            new_dict["parole"].append(element)
    return new_dict


input_utente = [1, "ciao", 3, "python", 7]
print(raggruppa_numeri_parole(input_utente))
print(raggruppa_numeri_parole2(input_utente))
