'''Descrizione: Dato un elenco di parole, raggruppale in un dizionario 
secondo la loro lunghezza.'''

def dizionario_secondo_lunghezza(parole: list[str]) -> dict[int, list[str]]:
    new_dict = {}
    for parola in parole:
        lunghezza_parola = len(parola)
        if lunghezza_parola not in new_dict:
            new_dict[lunghezza_parola] = [parola]
        else:
            new_dict[lunghezza_parola] += [parola]
    dizionario_ordinato = dict(sorted(new_dict.items()))
    return dizionario_ordinato



input_utente = ['ciao', 'a', 'gatto', 're', 'cane']
print(dizionario_secondo_lunghezza(input_utente))