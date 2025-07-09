def numero_magico(n: int) -> bool:
    somma = 0
    for item in str(n):
        somma += int(item)
    
    if somma % 7 == 0:
        return True 
    else:
        return False 
    
print(numero_magico(133))
print(numero_magico(91))

def numero_magico(n:int) -> bool:
    return sum(int(c) for c in str(n)) % 7 == 0