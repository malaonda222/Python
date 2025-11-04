'''Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51'''

for i in range(1, 8):
    print(i)

for i in range(3, 24, 5):
    print(i)

for i in range(20, -11, -6):
    print(i)

for i in range(19, 52, 8):
    print(i)


# oppure


i = 1 
while i <= 7:
    print(i)
    i += 1

i = 3 
while i <= 23:
    print(i)
    i += 5 

i = 20 
while i >= -10:
    print(i)
    i -= 6 

i = 19 
while i <= 51:
    print(i)
    i += 8