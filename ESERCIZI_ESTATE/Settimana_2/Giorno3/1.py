'''Dato un testo, crea un dizionario con la frequenza delle parole.'''

testo: str = "C'era una volta una ragazza con i capelli rossi. La ragazza viveva con il padre nel castello"
parole = testo.split()
dizionario: dict = {parola: parole.count(parola) for parola in set(parole)}

print(dizionario)


from collections import Counter 

testo: str = "mangiare bere dormire mangiare tutto a pranzo e a cena"
parole = testo.split()
conteggio = Counter(parole)
diz: dict = {parola: conta for parola, conta in conteggio.items() if conta >= 2}
print(diz)