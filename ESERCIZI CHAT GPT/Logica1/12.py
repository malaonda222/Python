def rec_fattoriale(numero: int) -> int|None:
    if numero < 0:
        return None 
    if numero == 0:
        return 1 
    else:
        return numero * rec_fattoriale(numero - 1)
    
print(rec_fattoriale(5))