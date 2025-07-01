lista1 = []
for i in range(2, 15, 2):
    lista1.append(i)
print(*lista1)


lista2 = []
i = 1
while i <= 13:
    lista2.append(i)
    i += 3
print(*lista2)


lista3 = []
for char in range(30, -1, -5):
    lista3.append(char)
print(*lista3)


lista4 = []
count = 5
while count <= 45:
    lista4.append(count)
    count += 10
print(*lista4)