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
