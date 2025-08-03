'''Trova il primo multiplo di 7 dopo 100'''

i = 101
while True:
    if i % 7 == 0:
        print(f"Il primo multiplo di 7 è: {i}")
        break
    i += 1

