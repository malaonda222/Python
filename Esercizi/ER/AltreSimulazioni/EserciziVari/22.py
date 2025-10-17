'''
Filtra e trasforma parole
 
Nome dell’esercizio: filter_and_reverse
Scrivi una funzione che:
* Prende in input una lista di stringhe words e una soglia intera min_len.
* Filtra solo le parole con lunghezza maggiore o uguale a min_len.
* Restituisce una nuova lista con le parole filtrate, invertite (cioè rovesciate carattere per carattere).
 
Esempio:
filter_and_reverse(["ciao", "ok", "python", "hi"], 3)
# ➜ ['oaic', 'nohtyp']
'''

def filter_and_reverse(words: list[str], min_len: int) -> list[str]:
    nuova_lista = []
    for word in words:
        if len(word) >= min_len:
            nuova_lista.append(word[::-1])
    return nuova_lista

print(filter_and_reverse(["fine", "del", "mondo"], 4))
print(filter_and_reverse(["ciao", "ok", "python", "hi"], 3))