'''Conta le parole uniche in un file (testuale o stringa simulata).'''

testo: str = "oggi oggi sono andato sono stato e ho dormito e mangiato"
parole = testo.split()
print({parola for parola in parole if parole.count(parola) == 1})

