# Funzione interna
def esterna(a:int, b:int):
        
    def interna(a:int, b:int) -> int:
        somma = a + b
        return somma

    # add = interna(a, b)
    # return add + 5
    # oppure
    return interna(a, b) + 5

print(esterna(2, 10))



def outer_fun(a, b):
    def addition(a, b):
        return a + b
    
    add = addition(a, b)
    return add + 5 

print(outer_fun(10, 5))
