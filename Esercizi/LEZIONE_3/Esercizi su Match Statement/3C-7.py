testa = 0
croce = 0
i = 0

print(f"Inserisci \"t\" o \"T\" oppure \"c\" o \"C\": ")
for x in range(8):
    lanci = input(f"Lancio {i + 1}: ")
    i += 1
    match lanci:
        case "t"|"T":
            testa += 1
        case "c"|"C":
            croce += 1
        case _:
            print(f"Input non riconosciuto. Inserire \"t\", \"T\" oppure \"c\", \"C\".")

percentuale_testa = (testa/8)*100
percentuale_croce = (croce/8)*100

print(f"Totale \"testa\": {testa}")
print(f"Percentuale \"testa\": {percentuale_testa:.2f}%")

print(f"Totale \"croce\": {croce}")
print(f"Percentuale \"croce\": {percentuale_croce:.2f}%")