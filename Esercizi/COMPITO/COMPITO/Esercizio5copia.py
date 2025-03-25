'''Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. 
Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.
Scrivere un programma che:
- Acquisisca in input un valore N (numero di euro disponibili).
- Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
- Mostri quanti buoni sconto avanzano al termine dell'acquisto.
Il programma deve continuare a scambiare i buoni con nuove barrette finché ce ne sono abbastanza per ottenere almeno una barretta gratuita.'''

euro_disponibili = int(input("Inserire il numero di euro disponibili: "))

buoni = euro_disponibili
barrette = euro_disponibili
barrette_totali = (euro_disponibili//6) + euro_disponibili
print(f"Il numero massimo di barrette è: {barrette_totali}.")

buoni_residui = euro_disponibili % 6
print(f"I buoni residui sono: {buoni_residui}")
