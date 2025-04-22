'''Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono 
essere rimossi come valori.'''

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:   
    nuova_lista = []
    for item in lista:
        if item in da_rimuovere and da_rimuovere[item] > 0:
            da_rimuovere[item] -= 1
        else:
            nuova_lista.append(item)
    return nuova_lista