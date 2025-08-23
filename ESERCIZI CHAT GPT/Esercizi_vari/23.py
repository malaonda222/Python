def sum_list(lista: list) -> int:
    somma = 0
    for i in lista:
        somma += i 
    return somma

print(sum_list([1, 8, 9, 3]))


def square_list(lista1: list) -> int:
    new_lista1 = []
    for i in lista1:
        square = i**2 
        new_lista1.append(square)
    return new_lista1

print(square_list([1, 5, 2, 3]))


def reverse_list(lista2: list) -> list:
    nuova_lista = []
    for i in range(len(lista2) -1, -1, -1):
        nuova_lista.append(lista2[i])
    return nuova_lista

print(reverse_list([8, 5, 9, 22]))


def count_vowels(s: str) -> int:
    s_lower = s.lower()
    count = 0
    for i in s_lower:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count += 1 
    return count 

print(count_vowels("Rigorosamente"))


def remove_duplicates(lista3: list) -> list:
    senza_duplicati = []
    for i in lista3:
        if i not in senza_duplicati:
            senza_duplicati.append(i)
    
    return senza_duplicati #oppure return list(set(lista3))

print(remove_duplicates([3, 5, 6, 6, 7, 7, 8, 9, 9]))