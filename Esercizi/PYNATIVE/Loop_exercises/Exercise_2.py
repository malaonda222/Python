# print the following pattern

# lista = []
# i = 1
# while i <= 5:
#     lista.append(i)
#     print(list)
#     i+=1

# lista = []
# for x in range(1, 6):
#     lista.append(x)
#     print(lista)


file = int(input("Inserisci il numero di file: "))
for i in range(1, file+1, 1): #quantità di righe che vogliamo
    for k in range(1, i+1): #inserisce gli elementi nella riga
        print(k, end= " ") #stampa il valore di k per ogni iterazione e mette uno spazio tra i numeri
    print() #crea una nuova riga 
