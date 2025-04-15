# Ritorna una lambda

def moltiplicatore(n:int) -> int:
    return lambda num: num * n

per_due = moltiplicatore(2)
print(per_due(10))



def moltiplicatore(n:int, m:int) -> int:
    return m * n 
 
print(moltiplicatore(8, 2))