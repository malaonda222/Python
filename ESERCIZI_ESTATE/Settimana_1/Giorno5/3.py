'''Scrivi una funzione che restituisce "pari" o "dispari".'''

def pari_dispari(n: int) -> str:
    if n % 2 == 0:
        return "Pari"
    else:
        return "Dispari"
    
print(pari_dispari(10))
print(pari_dispari(21))
