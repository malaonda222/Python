def recursive_fattoriale(n: int):
    if n < 0: 
        raise ValueError("Il numero non deve essere negativo")
    if n == 0:
        return 1
    else:
        return n*recursive_fattoriale(n-1)

print(recursive_fattoriale(5))