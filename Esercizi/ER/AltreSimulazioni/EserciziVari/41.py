'''Esercizio: Invertire l'ordine delle parole in una stringa
Obiettivo:
Scrivi una funzione che prenda una stringa, separi le parole, le inverta nell'ordine (ma non le inverta singolarmente) e 
poi restituisca la stringa modificata.

Indicazioni:
La stringa può contenere più parole separate da spazi.
Se la stringa è vuota, restituisci un messaggio di errore.
Mantieni l'ordine originale delle lettere nelle singole parole, ma inverti solo l'ordine delle parole.

Esempio:
Input: "ciao mi chiamo Lisa"
Output: "Lisa chiamo mi ciao"'''

def inverti_ordine_stringa(stringa: str) -> str:
    if not stringa:
        return "Errore, stringa vuota"
    
    parole = stringa.split() #suddivido la stringa in parole
    parole_invertite = parole[::-1] #inverto l'ordine delle parole

    nuova_stringa = " ".join(parole_invertite)
    return nuova_stringa


print(inverti_ordine_stringa("ciao mi chiamo Lisa"))
