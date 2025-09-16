'''Scrivi una funzione che prende una lista di numeri interi e restituisce 
quante sottosequenze crescenti consecutive contiene.
Una sottosequenza crescente consecutiva è una serie di numeri dove ogni numero 
è strettamente maggiore del precedente.'''

def conta_sequenze_crescenti(lista_numeri: list[int]) -> int:
    if len(lista_numeri) < 2: 
        return 0
    
    sottosequenze = 0
    in_sequenza = False
    for i in range(len(lista_numeri)):
        if lista_numeri[i] > lista_numeri[i - 1]:
            if not in_sequenza:
                sottosequenze += 1
                in_sequenza = True 
            else:
                in_sequenza = False  
    return sottosequenze
            

print(conta_sequenze_crescenti([1, 2, 3, 1, 2, 1, 5, 6]))