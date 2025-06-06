def fattoriale(n: int) -> int:
    factorial: int = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1 
    return factorial

print(fattoriale(100))


def fattoriale1(n: int) -> int:
    factorial2: int = 1
    for i in range(n):
        factorial2 *= n - i
    return factorial2


def factorial(n: int) -> int:
    if n == 1:
        return n
    else:
        return factorial(n-1) * n
