# Ordinal Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in numbers:
    if x == 1:
        print(f"{x}st")
    if x == 2:
        print(f"{x}nd")
    if x == 3:
        print(f"{x}rd")
    elif x >= 4 and x <= 9:
        print(f"{x}th")

lista = []
for number in range(1, 10):
    lista.append(number)
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

