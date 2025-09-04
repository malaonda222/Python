'''Data una lista di parole, restituisci una lista di parole in 
maiuscolo ma solo se più lunghe di 3 lettere.'''

def maiuscolo(parole: list[str]) -> list[str]:
    return [parola.upper() for parola in parole if len(parola) > 3]


parole = ['ciao', 'a', 'tutti', 'voi', 'da', 'GPT']
print(maiuscolo(parole))