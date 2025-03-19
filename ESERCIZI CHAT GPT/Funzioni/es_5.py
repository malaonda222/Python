def pari_o_dispari(a:int):
    if a % 2 == 0:
        return "Pari"
    else:
        return "Dispari"
    

while True:
    numero = input("Inserisci un numero: ") 
    if numero.lstrip('-').isdigit():
        numero = int(numero)
        break 
    else:
        print("Inserire un numero intero positivo.")

risultato = pari_o_dispari(numero)
print(risultato)