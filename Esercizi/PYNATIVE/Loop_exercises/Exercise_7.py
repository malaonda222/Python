# Print the following pattern

# numero = int(input("Inserisci un numero: "))
# lista = [5, 4, 3, 2, 1]
# for x in lista:
#    print(lista)
#    lista.pop(0)


file = int(input("Inserisci il numero di file: "))
for i in range(0, file):
   for j in range(file-1, 0, -1):
      print(j, end= " ")
   print()