'''Logica: Implementa FizzBuzz da 1 a 100:
    Multipli di 3: “Fizz”
    Multipli di 5: “Buzz”
    Multipli di entrambi: “FizzBuzz”'''

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        i += 1
    elif i % 3 == 0:
        print("Fizz")
        i += 1
    elif i % 5 == 0:
        print("Buzz")
        i += 1
    else:
        print(i)
        i += 1
