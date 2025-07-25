'''Scrivi una funzione trova_massimo(lista: list[int | float]) -> int | float
che restituisce il numero più grande presente nella lista.'''

def trova_massimo(lista_numeri: list[int | float]) -> int|float:
    if not lista_numeri:
        raise ValueError("Errore. La lista è vuota.")
    massimo = lista_numeri[0]
    for item in lista_numeri[1:]:
        if item > massimo:
            massimo = item
    return massimo

print(trova_massimo([1, 3, 4]))


'''Scrivi una funzione elimina_duplicati(lista: list[int]) -> list[int]
che riceve una lista di interi e restituisce una nuova lista senza duplicati, 
mantenendo l’ordine originale.'''

def elimina_duplicati(lista: list[int]) -> list[int]:
    nuova_lista = []
    for element in lista:
        if element not in nuova_lista:
            nuova_lista.append(element)
    return nuova_lista

print(elimina_duplicati([1, 5, 6, 8, 1, 6, 5]))



'''Scrivi una funzione media_pari(lista: list[int]) -> float
che restituisce la media di tutti i numeri pari presenti nella lista.'''

def media_pari(lista: list[int]) -> float:
    if not lista: 
        raise ValueError("Lista vuota. Errore.")
    somma_pari = 0
    cont_pari = 0
    for element in lista:
        if element % 2 == 0:
            somma_pari += element 
            cont_pari += 1
    if cont_pari == 0:
        return "Nessun numero pari nella lista!"
    return f"Media: {somma_pari/cont_pari:.2f}"  

print(media_pari([2, 5, 8, 666, 3, 2]))  