# Print the following pattern

# numero = int(input("Inserisci un numero: "))
# lista = [5, 4, 3, 2, 1]
# for x in lista:
#    print(lista)
#    lista.pop(0)


file = int(input("Inserisci il numero di file: "))
lunghezza = int(input("Inserisci la lunghezza della riga: "))
for i in range(1, +1):
   for j in range(lunghezza-i, 0, -1):
      print(j, end= ' ')