# Distribuzione di una borsa di studio
reddito = float(input("Inserisci il reddito dello studente: "))
media = float(input("Inserisci la media dei voti dello studente:"))

if reddito < 20000 and media > 27:
    print("Borsa di studio approvata.")
else: 
    if reddito > 20000:
        print("Borsa si studio rifiutata. (Motivo: reddito troppo alto.")
    elif media < 27:
        print("Borsa si studio rifiutata. (Motivo: media insufficiente.")
