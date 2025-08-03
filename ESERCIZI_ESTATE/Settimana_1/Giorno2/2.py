'''Conta quante vocali sono presenti in una stringa.'''

def conta_vocali(stringa1: str) -> int:
    vocali: list = ["a", "e", "i", "o", "u"]
    contatore_vocali = 0
    for char in stringa1.lower():
        if char in vocali:
            contatore_vocali += 1
    return contatore_vocali

print(conta_vocali("Fifone"))

def conta_vocali_lc(stringa2: str) -> int:
    return sum(1 for char in stringa2.lower() if char in "aeiou")

print(conta_vocali_lc("Fifone"))


