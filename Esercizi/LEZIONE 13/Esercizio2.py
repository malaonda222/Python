'''Si supponga di voler calcolare l'ammontare del denaro depositato su un conto bancario ad interesse composto. Se m è la somma depositata sul conto, la somma disponibile alla fine del mese sarà 1.005 volte m.
Scrivere una funzione ricorsiva compoundInterest che calcoli la somma presente sul conto dopo t mesi data una somma di partenza m.'''

def compoundInterest(m: float, tempo:int) -> float:
    if m == 0:
        return "Errore. Deve investire una somma."
    if tempo <= 0: #non è passato ancora un mese da quanto ho depositato il saldo m, quindi il saldo sarà m
        return round(m, 2)
    else:
    # se t=1(è passato un mese) il saldo sul conto sarà 1.005*m, se m=1000 il saldo sarà 1.005*1000 = 1000
    # se t=2, 1005 * 1.005 = 1010,03
    # se t=3, 1010,03 * 1.005 = 1015,08
        return round(1.005 * compoundInterest(m, tempo-1), 2)
    
print(compoundInterest(1000, 9))


def compoundInterest(m: float, tempo:int, tasso:float) -> float:
    if m == 0:
        return "Errore. Deve investire una somma."
    if tempo <= 0: 
        return round(m, 2)
    else:
        return round(tasso * compoundInterest(m, tempo - 1), 2)
    
print(f"{compoundInterest(1000, 3, 1.005)}")



def compoundInterest(m:int, mese:int) -> int:
    if mese == 0:
        return m 
    if m <= 0:
        return "Versare una somma sul conto."
    else:
        return int(1.005 * compoundInterest(m, (mese-1)))
    
print(compoundInterest(1900, 4))