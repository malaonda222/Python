def somma(a: float, b: float) -> float:
    risultato = a + b 
    return risultato 

print(somma(5, 8))


def somma_lista(lista_numeri: list[int|float]) -> int|float:
    risultato = 0
    for item in lista_numeri:
        risultato += item 
    return risultato

print(somma_lista([4, 6, 8, 1100, 367]))


def massimo_tre(a: int|float, b: int|float, c: int|float) -> int|float:
    return max(a, b, c)

def massimo_tre(a: int|float, b: int|float, c: int|float) -> int|float:
    lista_numeri = [a, b, c]
    max = lista_numeri[0]
    for item in lista_numeri:
        if item > max:
            max = item
    return max


print(massimo_tre(3, 6, 5))


def media_lista(lista_num: list[int|float]) -> float:
    if not lista_num:
        return 0
    somma = 0
    contatore_num = 0
    for element in lista_num:
        somma += element 
        contatore_num += 1
    return f"Media: {somma/contatore_num}"

print(media_lista([4, 5, 102, 22, 4]))



def quadrato_num() -> int:
    numero = int(input("Inserisci un numero intero: "))
    if numero == 0:
        return 0
    else:
        quadrato = numero**2
        return f"Il quadrato è: {quadrato}"
print(quadrato_num())



def conta_vocali(s: str) -> int:
    vocali = ["a", "e", "i", "o", "u"]
    contatore = 0
    lower_s = s.lower()
    for item in lower_s:
        if item in vocali:
            contatore += 1 
    return contatore

print(conta_vocali("Ciao, come stai?"))


somma_numeri = 0
while True:
    valore = input("Inserisci un numero intero: ")
    if valore.lower() == 'stop':
        break 
    try: 
        valore = int(valore)
        somma_numeri += valore 
    except ValueError:
        print("Inserisci un numero intero: ")
    
print(f"La somma è: {somma_numeri}") 