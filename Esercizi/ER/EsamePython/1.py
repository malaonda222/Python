'''Scrivi una funzione che prende in input una stringa (s) e restituisce la stringa invertita. reverse_string(s: str) -> str: 
se s="ciao" la funzione deve restituire "oaic"'''

def reverse_string(s: str) -> str:
    invertita = ""
    i = len(s) - 1
    while i >= 0:
        invertita += s[i]  # Aggiungi il carattere invertito alla stringa
        i -= 1  # Decrementa l'indice per andare al carattere precedente
    return invertita


