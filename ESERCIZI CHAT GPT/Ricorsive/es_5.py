def recursive_sum(n: int) -> int:
    if n < 0 or n % 1 != 0:
        raise ValueError("Il numero non può essere negativo o non intero")
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n-1)
    
print(recursive_sum(5))