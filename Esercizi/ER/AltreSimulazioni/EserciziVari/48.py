'''Scrivere una funzione che ordina solo i numeri pari di una lista, mantenendo i 
numeri dispari nelle loro posizioni originali.
Data una lista di numeri interi, la funzione deve:
- identificare tutti i numeri pari e le posizioni nella lista
- ordinare solo i numeri pari in ordine crescente
- reinserire i numeri pari ordinati nelle posizioni originali
- lasciare i numeri dispari invariati nelle loro posizioni'''

def ordina_solo_pari(numbers: list[int]) -> list[int]:
    lista_pari = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            lista_pari.append(i)

    if lista_pari:
        numeri_pari = []
        for index in lista_pari:
            numero = numbers[index]
            numeri_pari.append(numero)

    n = len(numeri_pari)
    for i in range(n):
        for j in range(0, n-i-1):
            if numeri_pari[j] > numeri_pari[j+1]:
                numeri_pari[j], numeri_pari[j+1] = numeri_pari[j+1], numeri_pari[j]
    
    risultato = numbers[:]
    for k in range(len(lista_pari)):
        risultato[lista_pari[k]] = numeri_pari[k]
    
    return risultato
    

print(ordina_solo_pari([1, 4, 5, 3, 7, 8, 2, 22, 6]))