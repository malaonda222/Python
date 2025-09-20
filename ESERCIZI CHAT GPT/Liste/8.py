'''Esercizio 8 - Ordinamento personalizzato
Tema: Ordinamento liste
Obiettivo: Ordinare in base a criterio
Traccia:
Scrivi una funzione che, data una lista di stringhe, ritorni una nuova lista ordinata in base alla lunghezza delle stringhe.'''

def ordinamento_personalizzato(lista_stringhe: list[str]) -> list[str]:
    return sorted(lista_stringhe, key=len)

def ordinamento_personalizzato(lista_stringhe: list[str]) -> list[str]:
    return sorted(lista_stringhe, key=len, reverse=True)

def ordinamento_crescente(lista_stringhe: list[str]) -> list[str]:
    n = len(lista_stringhe)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(lista_stringhe[j]) > len(lista_stringhe[j+1]):
                lista_stringhe[j], lista_stringhe[j+1] = lista_stringhe[j+1], lista_stringhe[j]
    return lista_stringhe 

def ordinamento_decrescente(lista_stringhe: list[str]) -> list[str]:
    n = len(lista_stringhe)
    for i in range(n):
        for j in range(n-i-1):
            if len(lista_stringhe[j]) < len(lista_stringhe[j+1]):
                lista_stringhe[j], lista_stringhe[j+1] = lista_stringhe[j+1], lista_stringhe[j]
    return lista_stringhe

def ordinamento_inbase_vocali(lista_stringhe: list[str]) -> list[str]:
    vocali = 'aeiouAEIOU'
    def count_vocali(s: str) -> int:
        return sum(1 for c in s if c in vocali)
    return sorted(lista_stringhe, key=count_vocali, reverse=True)

def ordinamento_sort(lista_stringhe: list[str]) -> list[str]:
    lista_stringhe.sort(key=len)
    return lista_stringhe


print(ordinamento_personalizzato(["ciao", "mi", "chiamo"]))
print(ordinamento_crescente(["cocomero", "banana", "mela", "kiwi", "uva"]))
print(ordinamento_decrescente(["cocomero", "banana", "mela", "kiwi", "uva"]))
print(ordinamento_inbase_vocali(["ciao", "mi", "chiamo"]))
print(ordinamento_sort(["ciao", "a", "bellissimo", "giornata", "animale"]))

