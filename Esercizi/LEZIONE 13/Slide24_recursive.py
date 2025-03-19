def RecursiveSum(n:int) -> int:
    if n < 0:
        print("Il numero deve essere positivo")
        return 0 #perché la mia somma non la posso calcolare
    elif n == 0:
        return 0
    else:
        return int(n + RecursiveSum(n-1))

    
print(RecursiveSum(5)) 