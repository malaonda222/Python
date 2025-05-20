def sum(n:int) -> None:
    if n < 0:
        print("Errore.")
    else:
        somma = 0
        i = 0
        while i <= n:
            somma += i 
            i = i + 1
        print(somma)
    

sum(-5)
sum(5)


def sum(n:int) -> int:
    if n < 0:
        print("Error! Inserted number is negative!")
        return 0
    else:
        somma = 0
        while n:
            somma = somma + n
            n = n-1
            return int(somma)