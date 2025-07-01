# Esercizio 9
'''Il valore di π può essere approssimato utilizzando la seguente serie infinita:
π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini sono necessari per ottenere approssimazioni 
sempre più accurate. 

Quindi:
- progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
- modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
- modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
- modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.

Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.'''

somma = 0
n = 0
trovato_314 = False
trovato_3141 = False
trovato_31415 = False
trovato_314159 = False
termini_314 = 0
termini_3141 = 0
termini_31415 = 0
termini_314159 = 0

# inserire ciclo while
while not trovato_314 or not trovato_3141 or not trovato_31415 or not trovato_314159:
    somma += 4 * ((-1)**n / (2*n + 1)) # formula di Leibniz per pi
    n = n + 1

    numero_troncato_2d = str(somma)[:4] 
    if numero_troncato_2d == "3.14" and not trovato_314: # condizione per primo caso (π ≈ 3.14)
        trovato_314 = True
        termini_314 = n
    numero_troncato_3d = str(somma)[:5]
    if numero_troncato_3d == "3.141" and not trovato_3141: # condizione per secondo caso (π ≈ 3.141)
        trovato_3141 = True
        termini_3141 = n
    numero_troncato_4d = str(somma)[:6]
    if numero_troncato_4d == "3.1415" and not trovato_31415: # condizione per terzo caso (π ≈ 3.1415)
        trovato_31415 = True
        termini_31415 = n
    numero_troncato_5d = str(somma)[:7]
    if numero_troncato_5d == "3.14159" and not trovato_314159: # condizione per quarto caso (π ≈ 3.14159)
        trovato_314159 = True
        termini_314159 = n
    
    # stampa di somma e numeri approssimati
    print(somma)
    print(numero_troncato_2d)
    print(numero_troncato_3d)
    print(numero_troncato_4d)
    print(numero_troncato_5d)

# stampa dei termini che devono essere usati per ottenere i vari casi di π
print(f"Il numero di termini della serie che devono essere usati per ottenere il valore di π ≈ 3.14 è: {termini_314}")
print(f"Il numero di termini della serie che devono essere usati per ottenere il valore di π ≈ 3.141 è: {termini_3141}")
print(f"Il numero di termini della serie che devono essere usati per ottenere il valore di π ≈ 3.1415 è: {termini_31415}")
print(f"Il numero di termini della serie che devono essere usati per ottenere il valore di π ≈ 3.14159 è: {termini_314159}")





