'''Logica: Trova la parola più frequente in un testo.'''

def piu_frequente(testo: list[str]) -> str:
    frequenza = {}
    for element in testo:
        if element not in frequenza:
            frequenza[element] = 1
        else:
            frequenza[element] += 1

    max_frequenza = 0
    parola_piu_frequente = ""
    for parola in frequenza:
        if frequenza[parola] > max_frequenza:
            max_frequenza = frequenza[parola]
            parola_piu_frequente = parola 

    return parola_piu_frequente


print(piu_frequente(["ciao", "ciao", "come", "va"]))