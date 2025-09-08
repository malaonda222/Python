def conteggio_cifre(n: int) -> int:
    n_str = str(n)
    if len(n_str) == 1:
        return 1 
    else:
        return 1 + conteggio_cifre(int(n_str[:-1]))
    

def conteggio_cifre2(n: int) -> int:
    if n < 10:
        return 1
    else:
        return 1 + conteggio_cifre(n//10)

print(conteggio_cifre(12345))
print(conteggio_cifre2(123456))
