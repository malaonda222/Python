'''Scrivi una funzione che controlla se una stringa ha le parentesi (), {}, [] bilanciate.'''

def bilanciamento(stringa: str) -> bool:
    if stringa.count("(") == stringa.count(")") and stringa.count("[") == stringa.count("]") and stringa.count("{") == stringa.count("}"):
        return True
    else:
        return False 
    
print(bilanciamento("(a + b) * [2 + {x - y}]"))
    
risultato = 0
contatore = 0
stringa = "(a + b) * [2 + {x - y}]"

for element in stringa: 
    if contatore >= 0:
        if element == "(":
            contatore += 1 
        if element == ")":
            contatore -= 1
        else:
            risultato = False
if contatore == 0:
    risultato = True 
else:
    risultato = False 
    
print(f"Parentesi Bilanciate: {risultato}")


