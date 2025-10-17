'''
Tema: Liste, conteggi, filter, lambda
 
Obiettivo: Isolare gli elementi unici in una lista (quelli che compaiono esattamente una volta)
Nome dell’esercizio: elementi_unici_assoluti
Traccia:
Scrivi una funzione che prende una lista di parole e restituisce una nuova lista 
contenente solo le parole che appaiono una sola volta, nell’ordine originale.
 
# Esempio:
parole = ["ciao", "mondo", "ciao", "python", "ciao", "codice", "python", "ciao", "logica"]
 
# Output atteso:
["mondo", "codice", "logica"]
 
Suggerimento:
Puoi usare un dizionario per contare le occorrenze, e poi usare filter con lambda per tenere solo quelle con count == 1.
'''

def elementi_unici_assoluti(words: list[str]) -> list[str]:
    my_dict = {}
    for word in words:
        if word not in my_dict:
            my_dict[word] = 1 
        else:
            my_dict[word] += 1 
    filtrati = list(filter(lambda word: my_dict[word] == 1, words))
    return filtrati 


def elementi_unici_assoluti1(words: list[str]) -> list[str]:
    my_dict = {}
    for word in words:
        if word not in my_dict:
            my_dict[word] = 1 
        else:
            my_dict[word] += 1 
    
    new_list = []
    for key in my_dict.keys():
        if my_dict[key] == 1:
            new_list.append(key)
    return new_list


def elementi_unici_assoluti2(words: list[str]) -> list[str]:
    return list(filter(lambda word: words.count(word) == 1, words))


parole = ["ciao", "mondo", "ciao", "python", "ciao", "codice", "python", "ciao", "logica"]

print(elementi_unici_assoluti(parole))
print(elementi_unici_assoluti1(parole))
