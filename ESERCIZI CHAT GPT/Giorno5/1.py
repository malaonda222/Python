'''Algoritmo di compressione con Run-Length Encoding (RLE) migliorato
Scrivi una funzione che comprime una stringa utilizzando un Run-Length Encoding 
avanzato: le lettere ripetute consecutivamente vengono compresse nel formato "NxL" 
dove N è il numero di ripetizioni e L è il carattere.
Se un carattere appare solo una volta, non deve essere modificato.'''

def compressione(stringa: str) -> str:
    if not stringa:
        return ""
    
    nuova_stringa = ""
    count = 1

    for i in range(1, len(stringa)):
        if stringa[i] == stringa[i - 1]:
            count += 1
        else:
            if count == 1:
                nuova_stringa += stringa[i-1]
            else:
                nuova_stringa += f"{count}x{stringa[i-1]}"
            count = 1
    if count == 1:
        nuova_stringa += stringa[-1]
    else:
        nuova_stringa += f"{count}x{stringa[-1]}"
    return nuova_stringa

print(compressione("aaabbcdddde"))
