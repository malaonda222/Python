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
for i in range(1, file+1, 1):
    for k in range(1, i+1):
        print(k, end= " ")
    print()
