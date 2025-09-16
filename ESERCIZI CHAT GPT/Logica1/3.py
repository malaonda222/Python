'''Scrivi una funzione che prenda una lista di numeri interi e restituisca True se la lista segue una sequenza alternata tra numeri pari e dispari, altrimenti False.
Una sequenza è alternata se:
Un numero pari è seguito da un dispari
E un dispari è seguito da un pari
Per tutta la lista'''

def sequenza_alternata(sequenza: list[int]) -> bool:
    for i in range(len(sequenza) - 1):
        if sequenza[i] % 2 == 0:
            if sequenza[i + 1] % 2 == 0:
                return False 
            else:
                continue 
        if sequenza[i] % 2 == 1:
            if sequenza[i + 1] % 2 == 1:
                return False 
            else:
                continue 
    return True 


def sequenza_alternata1(sequenza: list[int]) -> bool:
    for i in range(len(sequenza) - 1):
        if sequenza[i] % 2 == sequenza[i + 1] % 2:
            return False 
    return True


print(sequenza_alternata([2, 3, 4, 5, 6]))
print(sequenza_alternata([1, 2, 3, 4, 5]))
print(sequenza_alternata([1, 1, 2, 4]))