'''Estrai i numeri pari da una lista.'''


lista_num = []
for i in range(5):
    numero: float = float(input("Inserisci un numero intero positivo: "))
    if numero < 0:
        print("Errore. Inserire un numero positivo!")
    else:
        if numero.is_integer():
            lista_num.append(int(numero))
        else:
            print("Errore. Inserire un numero intero!")


print(f"I numeri pari della lista sono: {[num for num in lista_num if num % 2 == 0]}")
