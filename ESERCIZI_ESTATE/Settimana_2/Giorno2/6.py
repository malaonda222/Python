'''Logica: Trova le parole palindrome in una lista.'''

parole: list = ["ciao", "bella", "radar", "anna", "polop"]
palindome: list = []
for parola in parole:
    if parola == parola[::-1]:
        palindome.append(parola)
print(palindome)