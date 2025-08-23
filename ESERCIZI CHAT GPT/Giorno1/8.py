'''Traccia:
Scrivi una funzione raggruppa_numeri_parole: list[int]) -> dict[str, list[int]] che, 
data una lista, ritorni un dizionario con chiavi: "numeri", "parole"'''


def raggruppa_numeri_parole(lista_generale: list[int, float, bool]) -> dict[str, list[int]]:
    nuovo_dizionario: dict = {"numeri": [], "parole": []}
    for element in lista_generale:
        if isinstance(element, (int, float, bool)):
            nuovo_dizionario["numeri"].append(element)
        if isinstance(element, str):
            nuovo_dizionario["parole"].append(element)
    return nuovo_dizionario

lista_generale: list = ["ciao", 5, 4, "come", "va", 10, 11, 18]
print(raggruppa_numeri_parole(lista_generale))