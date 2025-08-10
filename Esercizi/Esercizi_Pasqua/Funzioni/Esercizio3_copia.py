'''Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono 
essere rimossi come valori.'''

def elimina_dati(lista_dati: list[str, int], diz_da_rimuovere: dict[str, int]) -> list[int]:
    nuova_lista: list = []
    for item in lista_dati:
        if item in diz_da_rimuovere and diz_da_rimuovere[item] > 0:
            diz_da_rimuovere[item] -= 1
        else:
            nuova_lista.append(item)
    return nuova_lista
