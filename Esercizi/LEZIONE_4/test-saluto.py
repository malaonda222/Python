# # import saluto importa tutto il modulo saluto
# import saluto 
# saluto.greet("Lisa")

# #possiamo rinominare la funzione che abbiamo richiamato 
# import saluto as s 
# s.greet("Federico")

# # se voglio importare solo la funzione greet dal modulo saluto e ignorare il resto del modulo saluto:
# from saluto import greet 
# greet("Daniele")

# #possiamo rinominare la funzione che abbiamo richiamato
# from saluto import greet as g
# g("Susanna")

def myfunc(a:int, b:int) : 
    return int(a + b)

result = myfunc(3, 10)
print(result)

