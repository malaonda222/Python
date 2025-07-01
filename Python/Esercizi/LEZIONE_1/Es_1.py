# Calcolo cateto di un triangolo rettangolo

import math
#chiedere all'utente di inserire ipotenusa e cateto
a:float = float(input("Inserisci il valore dell'ipotenusa \"a\": "))
b:float = float(input("Inserisci il valore del cateto \"b\": "))

#condizione a>b e tutti gli altri casi 
if a>b:
    c = ((a**2) - (b**2)) **0.5
    c = math.sqrt((a**2) - (b**2))
    print(f"Il valore del cateto \"c\" è: {c}")
else:
    print("Errore!")

