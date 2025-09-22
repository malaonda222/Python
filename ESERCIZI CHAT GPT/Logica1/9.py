'''Scrivi una funzione che conta quante vocali (a, e, i, o, u) ci sono in una stringa.'''

def conta_vocali(stringa: str) -> int| None:
    vocali = "aeiouAEIOU"
    conteggio = 0
    if not isinstance(stringa, str) or stringa.strip() == "":
        raise ValueError("Errore. Stringa non valida")
    else:
        for lettera in stringa:
            if lettera in vocali:
                conteggio += 1 
        return conteggio 
    

def conta_vocali1(stringa: str) -> int| None:
    vocali = "aeiou"
    conteggio = {v: 0 for v in vocali}
    if not isinstance(stringa, str) or stringa.strip() == "":
        raise ValueError("Errore. Stringa non valida")
    else:
        for lettera in stringa.lower():
            if lettera in vocali:
                conteggio[lettera] += 1
        return conteggio 

print(conta_vocali("Ciao Mondo"))
print(conta_vocali1("Ciao Mondo"))
