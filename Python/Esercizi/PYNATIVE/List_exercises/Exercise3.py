'''Trasforma ogni elemento di un elenco nel suo quadrato'''

numbers = [1, 2, 3, 4, 5, 6, 7]

squares = [num*num for num in numbers]
print(squares)

quadrati = []
for i in numbers:
    quadrati.append(i*i)
print(quadrati)
