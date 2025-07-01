# chiedere all'utente di inserire un voto
voto = int(input("Inserire un voto numerico da 1 a 10: "))

# match statement
match voto:
    case 10:
        print("Eccellente")
    case 8|9: 
        print("Molto buono")
    case 7|8:
        print("Sufficiente")
    case voto if voto > 0 and voto < 4:
        print("Gravemente insufficiente")
    case _:
        print("Voto non valido")

    