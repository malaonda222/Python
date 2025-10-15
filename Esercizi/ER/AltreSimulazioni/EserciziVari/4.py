'''
Esercizio: Funzione compute_lengths
 
Scrivi una funzione con il seguente header:
* compute_lengths(strings: list[str]) -> dict[str, float]
che, data una lista di stringhe, ritorni un dizionario con tre chiavi:
    * "shortest" -> lunghezza della stringa più corta
    * "longest" -> lunghezza della stringa più lunga
    * "average" -> lunghezza media delle stringhe (somma delle lunghezze diviso numero di stringhe)
 
Se la lista è vuota, solleva un'eccezione ValueError con messaggio "lista vuota".
Vincolo:
I valori di "shortest", "longest" e "average" non possono essere calcolati usando 
funzioni built-in come min(), max() o sum(), né altre librerie esterne.
'''

def compute_lengths(strings:list[str]) -> dict[str, float]:
    if not strings:
        raise ValueError("Lista vuota.")
    else:
        corta = strings[0]
        lunga = strings[0]
        somma = 0
        for stringa in strings:
            if len(stringa) < len(corta):
                corta = stringa 
            elif len(stringa) > len(lunga):
                lunga = stringa 
            somma += len(stringa)
        
        media = somma / len(strings)
        return {
            "shortest": float(len(corta)),
            "longest": float(len(lunga)), 
            "average": media
        }
    

def compute_lengths1(strings: list[str]) -> dict[str, float]:
    if strings == []:
        raise ValueError("Lista vuota")
    else:
        somma = 0
        piu_corta = len(strings[0])
        piu_lunga = len(strings[0])
        for stringa in strings:
            lunghezza = len(stringa)
            if lunghezza > piu_lunga:
                piu_lunga = lunghezza 
            elif lunghezza < piu_corta:
                piu_corta = lunghezza 
            somma += lunghezza 
        media = somma / len(strings)
        return {
            "shortest": float(piu_corta),
            "longest": float(piu_lunga),
            "average": float(media)
        }


strings = ["ciao", "oggi", "fa", "caldissimo"]
print(compute_lengths(strings))

strings1 = ["buongiorno", "mi", "chiamo", "Antonio"]
print(compute_lengths1(strings1))