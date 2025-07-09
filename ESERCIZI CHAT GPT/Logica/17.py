def riga_valida(lista: list[int]) -> bool:
    if len(lista) != 9:
        return False 
    
    for i in lista:
        if i < 1 or i > 9:
            return False 
        
    if len(set(lista)) != 9:
        return False  

    return True

print(riga_valida([5, 3, 1, 6, 9, 2, 7, 4, 8]))