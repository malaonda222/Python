# chiedere all'utente di inserire il numero di neonati
neonati = int(input("Inserire il numero di neonati: "))

# match statement
match neonati:
    case 1:
        print("Congratulazioni!")
    case 2:
        print("Wow! Gemelli!")
    case 3:
        print("Wow! Tre!")
    case 4:
        print("Mamma mia Quattro! Wow!")
    case 5:
        print("Incredibile! Cinque!")
    case _:
        print(f"Complimenti! {neonati} bambini!")