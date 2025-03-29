'''Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.

Suggerimento: ogni volta che si effettua una chiamata ricorsiva, si utilizzi lo slicing per ottenere una nuova stringa formata dai caratteri compresi tra il secondo e l'ultimo della stringa originale.
L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.'''

def vowelsCounter(my_string:str) -> int:
    if my_string == "":
        return 0
    else:
        if my_string[0] == "a" or my_string[0] == "e" or my_string[0] == "i" or my_string[0] == "o" or my_string[0] == "u":
        #oppure: if my_string[0] in "aeiouAEIOU" 
            return 1 + vowelsCounter(my_string[1:])
        else:
            return vowelsCounter(my_string[1:])
    
print(vowelsCounter("aiuto"))
print(vowelsCounter("servire"))
print(vowelsCounter("terriero"))


def vowelsCounter(stringa_1:str) -> int:
    if stringa_1 == "":
        return ""
    else: 
        if stringa_1[0] in "aeiou":
            return 1 + vowelsCounter(stringa_1[1:])
        else:
            return vowelsCounter(stringa_1[1:])
