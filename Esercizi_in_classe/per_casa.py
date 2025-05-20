# a = [3, 2, 5]
# #scambiare i valori

# for i in range(len(a)):
#     for j in range(len(a)):
    
#         if a[i] <= a[j]:
#             print("ok")

#         else:
#             temp1 = a[i] 
#             a[i] = a[j] #come, come
#             a[j] = temp1 #ciao


'''Crea un algoritmo che prenda una lista disordinata di interi e resituisca una lista 
ordinata in ordine crescente senza usare funzioni.
Usare debugger''' 

def ordinare(lista_disordinata: list) -> list[int]:
    for i in range(len(lista_disordinata)):
        print(f"\nPassaggio {i}")
        for j in range(0, len(lista_disordinata) - 1):
            print(f"Confronto: lista[{j}] = {lista_disordinata[j]} con lista[{j + 1}] = {lista_disordinata[j + 1]}")
            if lista_disordinata[j] > lista_disordinata[j+1]:
                temp1 = lista_disordinata[j]
                lista_disordinata[j] = lista_disordinata[j+1]
                lista_disordinata[j+1] = temp1
                print(f"Scambio -> lista: {lista_disordinata}")
            else:
                print(f"Nessun scambio -> lista: {lista_disordinata}")
    return lista_disordinata

print(ordinare([10, 1, 14, 22, 23, 23]))        
