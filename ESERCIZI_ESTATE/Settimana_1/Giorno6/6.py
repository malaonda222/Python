'''Logica: Simula il gioco del numero da indovinare tra 1 e 100 con feedback “troppo alto/basso”.'''

import random 

# while True:
#     numero_da_indovinare = input("Inserisci il numero da indovinare: ")
#     try:
#         numero_da_indovinare = int(numero_da_indovinare)
#         if numero_da_indovinare < 1 or numero_da_indovinare > 100:
#             print("Errore. Il numero deve essere compreso tra 1 e 100")
#         else:
#             print(f"Hai inserito: {numero_da_indovinare}")
#             break
#     except ValueError:
#         print("Prego inserire un input valido!")

numero_da_indovinare: int = random.randint(1, 10)

i = 1
trovato = False
while i <= 5:
    tentativo = input("Prova a indovinare il numero: ")
    try: 
        tentativo = int(tentativo)
        if tentativo < 1 or tentativo > 10:
            print("Il numero deve essere compreso tra 1 e 10, riprova")
            continue
        if tentativo == numero_da_indovinare:
            print("Hai indovinato il numero!")
            break
        if i == 5:
            break
        elif tentativo > numero_da_indovinare:
            print("Troppo alto, ritenta!")
        elif tentativo < numero_da_indovinare:
            print("Troppo basso, ritenta!") 
        i += 1
    except ValueError:
        print("Inserisci un valore valido (numero tra 1 e 10)")

if tentativo != numero_da_indovinare:
    print("Hai esaurito i tentativi!")
    print(f"Il numero da indovinare era: {numero_da_indovinare}")