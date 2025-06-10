def ricerca_binaria(lista: list[int], n: int) -> bool:
    for item in lista:
        if type(item) != int:
            raise ValueError("La lista contiene caratteri diversi da interi.")
        else:
            continue 
    
    inizio = 0
    lista_ordinata = sorted(lista)
    fine = len(lista_ordinata) - 1
    
    while inizio <= fine:
        medio = (inizio + fine) // 2
        if n == lista_ordinata[medio]:
            return True
        if n > lista_ordinata[medio]:
            inizio = medio + 1
        else:
            fine = medio - 1
    return False
        
input_utente = ricerca_binaria([1, 2, 87, 6, 50, 9, 10, 11, 27, 88, 100, 101], 11)
print(input_utente)

input2_utente = ricerca_binaria([8, 9, 55, 69, 400, 6785, 8995, -3], 7)
print(input2_utente)
