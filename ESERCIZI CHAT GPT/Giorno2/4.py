'''Scrivi una funzione che, data una lista di stringhe, ritorni un dizionario in cui:
Le chiavi sono le lunghezze delle stringhe.
I valori sono liste di stringhe che hanno quella lunghezza.'''

def raggruppa_per_lunghezza(parole: list[str]) -> dict[int, list[str]]:
    new_dict = {}
    for parola in parole: 
        lunghezza_parola = len(parola)
        if lunghezza_parola not in new_dict:
            new_dict[lunghezza_parola] = []
        new_dict[lunghezza_parola].append(parola) 
    return new_dict

parole = ["casa", "sole", "luna", "albero", "mare", "uovo", "no", "sì", "montagna"]
print(raggruppa_per_lunghezza(parole))