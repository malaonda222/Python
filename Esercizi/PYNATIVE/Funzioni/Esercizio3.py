# Multiple values
def calculation(a:int, b:int):
    addition = a + b
    substraction = a - b 
    return addition, substraction 

res = calculation(40, 10)
print(res)


def calculation(a, b):
    return a + b, a - b 

add, sub = calculation(40, 10)
print(add, sub)