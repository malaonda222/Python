# Esercizio 5
'''Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. Ogni barretta 
acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.
Scrivere un programma che:
- Acquisisca in input un valore N (numero di euro disponibili).
- Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
- Mostri quanti buoni sconto avanzano al termine dell'acquisto.
Il programma deve continuare a scambiare i buoni con nuove barrette finché ce ne sono abbastanza per ottenere almeno una barretta gratuita.'''

# chiedere all'utente di inserire un valore N
N = int(input("Inserisci il numero di euro disponibili: "))

# calcolo per numero massimo di barrette
buoni = N
barrette = N
barrette_totali = N + (N//6)
print(f"Il numero massimo di barrette è: {barrette_totali}")

# verifica dei buoni residui
buoni_residui = N % 6
print(f"Numero di buoni residui: {buoni_residui}")



    

