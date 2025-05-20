def SumInRange (a:int, b:int) -> None:
    if a > b:
        temp:int = a #definire una variabile temporanea
        a = b 
        b = temp
        somma = 0
        while b >= a:
            somma = somma + b
            b = b - 1
        return int(somma)

print(SumInRange(5, 10))






