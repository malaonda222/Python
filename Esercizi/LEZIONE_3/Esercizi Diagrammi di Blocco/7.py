# Algoritmo per il calcolo della media dei voti con inserimento iterativo
cont = 0
sum = 0


while True:
    scelta = (input("Vuoi inserire un voto? "))
    if scelta == "si":
        voto = int(input("Inserisci un voto: "))
        if voto > 0: 
            cont = cont + 1
            sum = sum + voto
        else:
            print("Errore.")
    elif scelta == "no":
        if cont > 0:
            media = sum / cont
            print(f"La media dei numeri è: {media}")
        else:
            print("Nessun voto inserito")
        