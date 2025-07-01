# Funzione ricorsiva
def ricorsiva():
    somma = 0
    for i in range(0, 11):
        somma += i
    return somma
    
print(ricorsiva())



def addition(num:int):
    if num: 
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)