def outer_fun():
    def inner_1():
        pass 
    def inner_2():
        print("Ciao")
    return inner_2 

dec = outer_fun()
dec()


# ho una funzione che quando viene chiamata su un'altra funzione, 
# crera una inner function, richiama la funzione originale; il 
# decoratore ritorna il riferimento alla inner function
def decorator(fun):
    def wrapper():
        print("ciao")
        fun()
    return wrapper 


def quad():
    print(2**2)

quad = decorator(quad)
#primo quad fa riferimento al wrapper 
#secondo quad fa riferimento alla funzione 
quad()
