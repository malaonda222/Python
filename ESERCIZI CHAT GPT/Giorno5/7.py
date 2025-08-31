def fattoriale(n: int) -> int:
    fattoriale = 1
    i = 1
    if n == 0:
        return 1
    else:
        while i <= n:
            fattoriale *= i
            i += 1 
    return fattoriale 

def recursive_fattoriale(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * recursive_fattoriale(n- 1)

print(fattoriale(5))
print(recursive_fattoriale(5))