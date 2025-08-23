'''Esercizio 2 - Elementi unici in lista
Scrivi una funzione elementi_unici(lista) che prende una lista e restituisce una nuova 
lista contenente solo gli elementi non ripetuti.
Esempio: elementi_unici([1, 2, 2, 3, 4, 4]) → [1, 3]'''

def elementi_unici(lista_numeri: list[int]) -> list[int]:
    lista_senza_duplicati = []
    for element in lista_numeri:
        if lista_numeri.count(element) == 1:
            lista_senza_duplicati.append(element)
    return lista_senza_duplicati


def elementi_unici2(lista_numeri: list[int]) -> list[int]:
    frequenze = {}
    for numero in lista_numeri:
        if numero not in frequenze:
            frequenze[numero] = 1 
        else:
            frequenze[numero] += 1 
    
    return [numero for numero in lista_numeri if frequenze[numero] == 1]

lista_numeri = [1, 2, 2, 3, 4, 4]
print(elementi_unici(lista_numeri))
print(elementi_unici2(lista_numeri))

