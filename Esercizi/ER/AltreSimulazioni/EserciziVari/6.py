'''Scrivi una funzione con il seguente header:
def analyze_strings(strings: list[str]) -> dict[str, str]
Obiettivo:
Dati in input una lista di stringhe, la funzione deve restituire un dizionario con:
"shortest" → la stringa più corta
"longest" → la stringa più lunga
"first_alphabetically" → la stringa che viene prima in ordine alfabetico
"last_alphabetically" → la stringa che viene ultima in ordine alfabetico

Vincoli:
Non usare funzioni built-in come min(), max(), sorted() o simili.
Non usare librerie esterne.
Se la lista è vuota, solleva un’eccezione ValueError con messaggio "lista vuota".'''

def analyze_strings(strings: list[str]) -> dict[str, str]:
    if len(strings) == 0:
        raise ValueError("Lista vuota.")
    else:
        piu_corta = strings[0]
        piu_lunga = strings[0]
        prima = strings[0]
        ultima = strings[0]

        for stringa in strings:

            # confronta lunghezza
            lunghezza = len(stringa)
            if lunghezza < len(piu_corta):
                piu_corta = stringa 
            elif lunghezza > len(piu_lunga):
                piu_lunga = stringa

            # confronta ordine alfabetico
            if stringa > ultima:
                ultima = stringa 
            elif stringa < prima:
                prima = stringa        
        
        return {
            "shortest": piu_corta,
            "longest": piu_lunga,
            "first_alphabetically": prima,
            "last_alphabetically": ultima
        }

