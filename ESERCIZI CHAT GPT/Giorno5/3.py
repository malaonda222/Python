def somma_cifre_numero(numero: int) -> int:
    somma_numeri = 0
    for element in str(numero):
        somma_numeri += int(element) 
    return somma_numeri

print(somma_cifre_numero(1234))