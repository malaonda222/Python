def cronometro(fun):
    def wrapper():
        import time 
        start = time.time() 
        fun()
        print(time.time() - start)
    return wrapper 

@cronometro 
def prova():
    for i in range(1000000):
        pass 

# si definisce la funzione prova 
# decorata con un cronometro 

#La funzione @cronometro equivale a dire:
# prova = cronometro(prova)

prova()





def cronometro(fun):
    def wrapper(*args):
        import time 
        start = time.time() 
        fun(*args)
        print(time.time() - start)
    return wrapper 

@cronometro 
def prova():
    for i in range(1000000):
        pass 

prova()