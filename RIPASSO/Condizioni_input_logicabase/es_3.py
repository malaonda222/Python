'''
Scrivi una funzione chiamata pari_dispari() che:
Chieda all’utente di inserire un numero intero. 
Restituisca:
"Pari" se il numero è divisibile per 2.
"Dispari" altrimenti.
'''

def pari_dispari() -> None:
    numero: int = int(input("Inserisci un numero intero: "))
    if numero % 2 == 0:
        print("Pari")
    else:
        print("Dispari")

pari_dispari()