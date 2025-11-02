'''Scrivi una funzione chiamata reverse_words che prenda una stringa e 
restituisca una nuova stringa con le parole invertite ma mantenendo 
l'ordine delle parole nella frase. Una "parola" è definita come una 
sequenza di caratteri separata da spazi.

Input:
Una stringa di testo sentence, che può contenere più parole.

Output:
Una nuova stringa in cui ogni parola è invertita, ma l'ordine delle parole rimane invariato.'''


def reverse_words(stringa: str) -> str:
    if not stringa:
        return "Errore. Stringa vuota"
    
    lista_parole_invertite = []
    parole = stringa.split()
    for parola in parole:
        nuova_parola = parola[::-1]
        lista_parole_invertite.append(nuova_parola)
        
    nuova_stringa = " ".join(lista_parole_invertite)
    return nuova_stringa 

print(reverse_words("ciao mi chiamo Lisa"))

