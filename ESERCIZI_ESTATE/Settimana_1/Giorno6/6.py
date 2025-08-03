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

numero_da_indovinare: int = random.randint(1, 101)

trovato = False
while True:
    tentativo = input("Prova a indovinare il numero: ")
    try: 
        tentativo = int(tentativo)
        if tentativo < 1 or tentativo > 100:
            print("Il numero è compreso tra 1 e 100, riprova")
        elif tentativo > numero_da_indovinare:
            print("Troppo alto, ritenta!")
        elif tentativo < numero_da_indovinare:
            print("Troppo basso, ritenta!")
        elif tentativo == numero_da_indovinare:
            print("Hai indovinato il numero!")
            break
    except ValueError:
        print("Inserisci un valore valido (numero tra 1 e 100)")

