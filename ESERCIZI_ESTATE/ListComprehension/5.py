'''Data una lista di numeri, restituisci una lista di stringhe dove:
Se il numero è divisibile per 3 → "Fizz"
Se è divisibile per 5 → "Buzz"
Se è divisibile per entrambi → "FizzBuzz"
Altrimenti → il numero come stringa'''

def fizzbuzz(lista_numeri: list[int]) -> list[str]:
    return [
        "FizzBuzz" if num % 15 == 0 
        else "Fizz" if num % 3 == 0 
        else "Buzz" if num % 5 == 0 
        else str(num) 
        for num in lista_numeri
        ]


numeri = list(range(1, 21))
print(fizzbuzz(numeri))

