def moltiplica_numeri(lista: list[int]) -> int:
    numero_soglia: int = 30
    risultato_moltiplicazione = 1
    for element in lista:
        if not isinstance(element, int):
            raise ValueError("I numeri della lista devono essere tutti interi.")
        else:
            if element < numero_soglia:
                risultato_moltiplicazione *= element 
            else:
                continue 

    return risultato_moltiplicazione

lista1 = [3, 6, 90, 4, 22, 0.6]
print(moltiplica_numeri(lista1))