'''Traccia:
Scrivi una funzione raggruppa_per_tipo(lista: list[Any]) -> dict[str, list[Any]] 
che prenda una lista mista e ritorni un dizionario con chiavi: "numeri", "stringhe", "altri" 
per raggruppare gli elementi in base al tipo.
 
Input:
lista = [1, "ciao", 3.5, True, "Python", None, 42]'''


from typing import Any
def raggruppa_per_tipo(lista: list[Any]) -> dict[str, list[Any]]:
    new_dict = {"numeri": [], "stringhe": [], "altri": []}
    for elemento in lista: 
        if isinstance(elemento, (int, float)) and not isinstance(elemento, bool):
            new_dict["numeri"].append(elemento) 
        elif isinstance(elemento, str):
            new_dict["stringhe"].append(elemento) 
        else:
            new_dict["altri"].append(elemento) 
    
    return new_dict


lista = [1, "ciao", 3.5, True, "Python", None, 42]
print(raggruppa_per_tipo(lista))