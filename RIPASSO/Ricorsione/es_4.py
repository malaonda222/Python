'''Scrivi una funzione ricorsiva somma_cifre(n) che calcoli la somma delle
cifre di un numero intero positivo.'''

def somma_cifre(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n % 10 + somma_cifre(n // 10)

print(somma_cifre(1234))