'''Scrivi una funzione che riceve in input una stringa e restituisce un dizionario che 
contiene per ogni parola quante volte compare nella frase.'''

def conta_lettere(testo: str) -> dict:
    new_dict = {}
    for element in testo:
        if element not in new_dict:
            new_dict[element] = 1
        else:
            new_dict[element] += 1
    return new_dict

frase = "ciao mondo ciao ciao python mondo"
print(conta_lettere(frase))


def conta_parole(text: str) -> dict:
    nuovo_dict = {}
    tokens = text.split(" ")
    for token in tokens:
        if token not in nuovo_dict:
            nuovo_dict[token] = 1
        else:
            nuovo_dict[token] += 1

    return nuovo_dict

sentence = "ciao mondo ciao ciao python mondo"
print(conta_parole(sentence))