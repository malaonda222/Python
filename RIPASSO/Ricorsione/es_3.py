'''Traccia:
Definisci la funzione prodotto_cifre_dispari(n: int) -> int che prende in input un 
numero positivo n e restituisce il prodotto di tutte le cifre dispari contenute 
nel numero.
Se non ci sono cifre dispari, restituisci 1'''

def recursive_prodotto_cifre_dispari(n: int):
    if n == 0:
        return 1

    if n < 0:
          raise ValueError("Errore.")
    
    cifra = n % 10
    resto = n // 10
    prodotto_restante = recursive_prodotto_cifre_dispari(resto)

    if cifra % 2 == 1:
        return cifra * prodotto_restante
    else:
        return prodotto_restante
