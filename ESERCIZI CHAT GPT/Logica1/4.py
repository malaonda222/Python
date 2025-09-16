'''Scrivi una funzione che prende in input una lista di interi e rimuove i numeri
consecutivi duplicati, lasciando solo una copia per ciascun gruppo di ripetizioni consecutive.'''

def rimuovi_doppi_consecutivi(lista_numeri: list[int]) -> list[int]:
    if not lista_numeri:
        return []
    nuova_lista = [lista_numeri[0]]
    for i in range(1, len(lista_numeri)):
        if lista_numeri[i] == lista_numeri[i - 1]:
            continue
        else:
            nuova_lista.append(lista_numeri[i])
    return nuova_lista


print(rimuovi_doppi_consecutivi([1, 1, 2, 2, 2, 3, 1, 1]))