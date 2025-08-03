'''Usa un ciclo while per sommare numeri finché l’utente non digita 0.'''

somma_numeri = 0
while True:
    numero = float(input("Inserisci un numero: "))
    if numero == 0:
        break 
    else:
        somma_numeri += numero 
print(somma_numeri)