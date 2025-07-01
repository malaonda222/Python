'''Esercizio 6'''
def remove_duplicates(lista:list) -> list:
    list_not_duplicati = []
    
    for item in lista:
        if item not in list_not_duplicati:
            list_not_duplicati.append(item)
    
    return list_not_duplicati   

print(remove_duplicates([1, 2, "a", 1, 2, "a"]))
