# Calculate the multiplication and sum of two numbers

number1 = int(input("Inserisci il primo valore: "))
number2 = int(input("Inserisci il secondo valore: "))

prodotto = number1*number2
somma = number1+number2

# if prodotto <= 1000:
#     print(f"Il prodotto dei due numeri è: {prodotto}")
# else:
#     print(f"La somma dei numeri è: {somma}")


def moltiplication_or_sum(number1, number2):
    product = number1*number2
    if product <= 1000:
        return product
    else:
        return somma

result = moltiplication_or_sum(20, 30)
print(f"Il risultato è: {result}")

result = moltiplication_or_sum(40, 30)
print(f"The result is: {result} ")