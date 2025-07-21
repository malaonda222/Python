'''Scrivi una funzione ricorsiva fibonacci(n) che restituisca l'n-esimo 
numero della sequenza di Fibonacci (partendo da fibonacci(0) = 0 e fibonacci(1) = 1).'''

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))