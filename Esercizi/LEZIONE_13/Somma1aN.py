# Calcolare la somma dei numeri da 1 a n
def somma_rec(n:int) -> None:
    if n == 1:
        return 1
    elif n < 0:
        print("Errore.")
    else:
        return n + somma_rec(n-1)
    
n = int(input("Inserisci un numero: "))
risultato = somma_rec(n)
print(f"La somma dei numeri da 1 a {n} è {risultato}.")