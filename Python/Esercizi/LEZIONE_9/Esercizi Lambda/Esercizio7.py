# Filtra parole corte 

import re

parole = ["cane", "gatto", "elefante", "ratto", "orso"] 

almeno_cinque_lettere = list(filter(lambda parola: len(parola) > 4, parole))
print(almeno_cinque_lettere)

cinque_lettere = list(filter(lambda parola: re.fullmatch(r'[a-zA-Z]{5,}', parola), parole))
print(cinque_lettere)


def cinque_letters(parole:list [str]) -> list[str]:
    cinque_lette = []
    for parola in parole:
        if len(parola) > 4:
            cinque_lette.append(parola)
    return cinque_lette
    
print(cinque_letters(parole))
