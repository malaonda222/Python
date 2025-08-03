'''Logica: Dato un elenco di parole, trova quella più lunga.'''

parole: list = ["ciao", "mi", "chiamo", "Elisabetta", "centododici", "anni"]

parola_piu_lunga: str = parole[0]
for parola in parole:
    if len(parola) > len(parola_piu_lunga):
        parola_piu_lunga = parola   
    else:
        continue
print(parola_piu_lunga)