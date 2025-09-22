'''Data una stringa, scrivi una funzione che restituisce il primo carattere 
che si ripete più di una volta.'''

def caratteri_ripetuti(stringa: str) -> str:
    for element in stringa:
        if stringa.count(element) >= 2:
            return element 
        
def caratteri_ripetuti1(stringa: str) -> str:
    visti = set()
    for element in stringa:
        if element in visti:
            return element 
        visti.add(element)
    return None  

def caratteri_ripetuti2(stringa: str) -> str:
    return next((element for element in stringa if stringa.count(element) >= 2), None)


print(caratteri_ripetuti("programmazione"))
print(caratteri_ripetuti1("programmazione"))
print(caratteri_ripetuti2("programmazione"))

