lista_tuple = [('Bob', 120.0), ('Carla', 90.0), ('Alice', 50.0)]
n = len(lista_tuple)

'''ordinare in modo decrescente'''
for i in range(n):
    for j in range(0, n-i-1):
        if lista_tuple[j][1] < lista_tuple[j+1]:
            lista_tuple[j], lista_tuple[j+1] = lista_tuple[j+1], lista_tuple[j]
 
'''ordinare in modo crescente'''
for i in range(n):
    for j in range(0, n-i-1):
        if lista_tuple[j][1] > lista_tuple[j+1][1]:
            lista_tuple[j], lista_tuple[j+1] = lista_tuple[j+1], lista_tuple[j]