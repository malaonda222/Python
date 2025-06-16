def calculateCharges(ore_parcheggio: float) -> float:
    costo_parcheggio = 2
    tariffa_extra = 0.5
    if ore_parcheggio <= 3:
        return f"{costo_parcheggio}" 
    elif ore_parcheggio > 3 and ore_parcheggio < 24:
        costo = (ore_parcheggio - 3) * tariffa_extra + costo_parcheggio
        return costo 
    elif ore_parcheggio == 24: 
        costo = 10
        return costo 
    else:
        return "Errore. Numero di ore inserite non valide"


car1 = calculateCharges(1.5)
car2 = calculateCharges(4.0)
car3 = calculateCharges(24.0)

veicoli = [("car1", 1.5), ("car2", 4.0), ("car3", 24.0)]

print(f"{'Car':<10}{'Hours':<10}{'Charge':<10}")


totale_ore = 0
totale_costo = 0
for car, ore in veicoli:
    costo = float(calculateCharges(ore))
    totale_costo += costo 
    totale_ore += ore 
    print(f"{car:<10}{ore:<10}{costo:<10}")
print(f"{'TOTAL':<10}{totale_ore:<10}{totale_costo:<10}")