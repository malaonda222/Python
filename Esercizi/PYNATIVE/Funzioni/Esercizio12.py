global_var = 10

def modifica_variabile():
    global global_var 
    print("Funzione interna:", global_var)
    global_var = 20
     

modifica_variabile()
print("Funzione esterna:", global_var)