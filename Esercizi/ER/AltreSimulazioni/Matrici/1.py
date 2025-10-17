'''
Tema: Matrici e cicli annidati
Obiettivo: Imparare a scorrere le righe e applicare operazioni riga per riga.
 
Nome dell’esercizio: somma_per_riga
 
Traccia:
Scrivi una funzione che, data una matrice (lista di liste di interi), 
restituisca una lista contenente la somma di ogni riga.
 
Esempio:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
→ risultato = [6, 15, 24]
 
Non usare sum()
'''

def somma_per_riga(matrice: list[list[int]]) -> list[int]:
    risultato = []
    for sottolista in matrice:
        somma = 0
        for num in sottolista:
            somma += num
        risultato.append(somma)
    return risultato


matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(somma_per_riga(matrice))