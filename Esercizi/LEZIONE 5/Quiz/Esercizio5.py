def even_odd_pattern(numbers:list[int]) -> list[int]:
    lista_pari = []
    lista_dispari = []
    
    for number in numbers:
        if number % 2 == 0:
            lista_pari.append(number)
        else: 
            lista_dispari.append(number)
    
    lista_ordinata = lista_pari + lista_dispari
    return lista_ordinata 


