'''Scrivi una funzione che, data una lista di stringhe, restituisca:
La stringa con più vocali
La stringa con meno vocali
Il numero totale di caratteri alfabetici (lettere) in tutte le stringhe
La prima stringa in ordine alfabetico inverso (Z-A)

Ignora eventuali spazi o simboli.
Considera solo le vocali: a, e, i, o, u (puoi usare .lower() per evitare problemi con le maiuscole).
Puoi usare isalpha() per verificare se un carattere è una lettera.'''

def conta_vocali(strings: list[str]) -> dict[str, str|int|float]:
    vocali = 'aeiou'

    stringa_piu_vocali = strings[0]
    stringa_meno_vocali = strings[0]
    
    max_vocali = 0
    min_vocali = float('inf')

    numero_totale_caratteri = 0
    ultima_stringa = strings[0]

    for stringa in strings:
        stringa_lower = stringa.lower()
        numero_vocali = 0
        for element in stringa_lower:
            if element not in vocali:
                continue 
            else:
                numero_vocali += 1
            
        if numero_vocali > max_vocali:
            max_vocali = numero_vocali
            stringa_piu_vocali = stringa

        elif numero_vocali < stringa_meno_vocali:
            min_vocali = numero_vocali
            stringa_meno_vocali = stringa 

        if stringa_lower > ultima_stringa:
            ultima_stringa = stringa
        
        for char in stringa:
            if char.isalpha():
                numero_totale_caratteri += 1

    return {"Stringa con più vocali": stringa_piu_vocali,
            "Stringa con meno vocali": stringa_meno_vocali,
            "Numero totale caratteri": numero_totale_caratteri,
            "Prima stringa in ordine alfabetico inverso": ultima_stringa}