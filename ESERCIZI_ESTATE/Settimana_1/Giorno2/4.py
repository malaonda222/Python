'''Concatena una lista di stringhe in una sola stringa separata da virgole'''

def concatena(lista_stringhe: list[str]) -> str:
    return ", ".join(lista_stringhe)

def concatena2(lista1: list[str]) -> str:
    if not lista1:
        return ""
    risultato = lista1[0]
    for i in lista1[1:]:
        risultato += ", " + i
    return risultato

print(concatena(["Ciao come stai", "tutto ok?"]))
print(concatena(["Stasera andiamo al cinema", "ti va?"]))
print()
print(concatena2(["Ciao come stai", "tutto ok?"]))
print(concatena2(["Stasera andiamo al cinema", "ti va?"]))



def concatena_stringhe(lista_stringhe: list[str]) -> str:
    return ", ".join(lista_stringhe)

def concatena_stringhe2(lista_str: list[str]) -> str:
    if not lista_str:
        return ""
    result = lista_str[0]
    for element in lista_str[1:]:
        result += ", " + element 
    return result

print(concatena_stringhe(["ciao a tutti", "mi chiamo Lola"]))
print(concatena_stringhe(["Oggi mi sento bene", "anche te?"]))
