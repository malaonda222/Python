# chiamata per valori di default

def total(w, x, y=10, z=20):
    return(w ** x) + y + z
print(total(2, 3)) # chiama la funzione totale mentre omette gli ultimi 2 valori
print(total(2, 3, 4)) # chiama la funzione totale mentre omette l'ultimo valore
print(total(2, 3, 4, 5)) # chiama la funzione totale con 4 valori in input
