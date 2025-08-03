'''Conta quanti numeri in una lista sono > di un valore dato'''

soglia = 13
lista_num = [1, 4, 666, 3, 2, 4, 99, 90, 34]
count = len([num for num in lista_num if num > soglia])
print(count)


numeri_maggiori_di_soglia = 0
for element in lista_num:
    if element > soglia:
        numeri_maggiori_di_soglia += 1
print(numeri_maggiori_di_soglia)