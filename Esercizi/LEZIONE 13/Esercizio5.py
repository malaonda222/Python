def recursiveArmonica(n:int) -> float:
    if n <= 0:
        return "Errore"
    if n == 1:
        return 1
    else:
        return round(1 / n * (recursiveArmonica(n-1)), 6)
    

print(recursiveArmonica(6))
print(recursiveArmonica(10))