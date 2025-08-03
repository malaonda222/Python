''' Rimuovi duplicati da una lista mantenendo l’ordine.'''

def rimuovi_duplicati(lista: list[int|str|float|bool]) -> list:
    nuova_lista = []
    for element in lista:
        if element not in nuova_lista:
            nuova_lista.append(element)
    print(f"Lista originale: {lista}\nLista senza duplicati: {nuova_lista}")

rimuovi_duplicati([4, 4, "fine", "fine", 4, 8, 9, 0.9, 4, 0.9, "ciao"])


