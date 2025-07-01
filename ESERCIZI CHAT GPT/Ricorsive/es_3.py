'''Scrivi una funzione ricorsiva che inverta una stringa.'''

def recursiveString(my_string:str) -> str:
    if my_string == "":
        return ""
    else:
        return my_string[-1] + recursiveString(my_string[:-1])
    
print(recursiveString("ciao"))