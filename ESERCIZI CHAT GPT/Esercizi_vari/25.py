'''Scrivi una funzione analizza_testo(testo: str) che restituisce:
    Numero totale di parole
    Numero di frasi (frasi terminate da ., !, ?)
    Top 3 parole più frequenti (ignorando maiuscole/minuscole e 
    punteggiatura)'''

def analizza_testo(testo: str):
    testo_minuscolo = testo.lower()
    numero_frasi = testo_minuscolo.count('.') + testo_minuscolo.count('!') + testo_minuscolo.count('?')
    for c in ['.', '!', '?', ',', ';', ':']:
        testo_minuscolo = testo_minuscolo.replace(c, '')
    
    parole = testo_minuscolo.split()
    numero_parole= len(parole)
    
    frequenze = {}
    for parola in parole:
        if parola not in frequenze:
            frequenze[parola] = 1
        else:
            frequenze[parola] += 1
    
    top_parole = sorted(frequenze, key=frequenze.get, reverse=True)[:3]
 
    return f"Parole totali: {numero_parole}\nFrasi: {numero_frasi}\nTop parole: {top_parole}"


print(analizza_testo("Ciao! Come stai? Io sto bene. Tu?"))
    
   
