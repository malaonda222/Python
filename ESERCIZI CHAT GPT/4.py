def somma(a:int, b:int):
    risultato = a+b
    return risultato

my_result = somma(3, 5)
print(f"La somma è: {my_result}")

def area_cerchio(raggio:int):
    area = 3.1459 * raggio**2
    return area

my_area = area_cerchio(5)
print(my_area)

def pari_o_dispari(numero:int):
    if numero %2 == 0:
        print("Il numero è pari.")
    else:
        print("Il numero è dispari.")

my_number = pari_o_dispari(2)
my_number1 = pari_o_dispari(7)

