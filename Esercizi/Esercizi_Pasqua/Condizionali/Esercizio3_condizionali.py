def calcola_stipendio(ore_lavorate: int) -> float:
    paga_oraria = 10
    paga_straordinaria = 15
    if ore_lavorate <= 40:
        return ore_lavorate*paga_oraria
    else:
        ore_straordinarie = (ore_lavorate - 40) * paga_straordinaria
        return ore_straordinarie + (40 * paga_oraria)
    

print(calcola_stipendio(40))
print(calcola_stipendio(0))
print(calcola_stipendio(60))
