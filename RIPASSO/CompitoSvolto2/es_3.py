'''Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono 
essere rimossi come valori.'''

def elimina_dati(lista: list[int], diz_da_rimuovere: dict[int, int]) -> list[int]:
    new_list = []
    for item in lista:
        if item in diz_da_rimuovere and diz_da_rimuovere[item] > 0:
            diz_da_rimuovere[item] - 1
        else:
            new_list.append(item)
    return new_list

print(elimina_dati([3, 4, 6, 5, 4, 6], {3: 1, 4: 1, 6: 2}))