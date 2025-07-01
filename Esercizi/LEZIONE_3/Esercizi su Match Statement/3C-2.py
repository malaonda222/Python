# chiedere all'utente il voto di laurea compreso tra 66 e 100
voto = int(input("Inserire un voto di laurea compreso tra 66 a 110: "))

# match statement
match voto:
    case voto if voto >= 106 and voto <= 110:
        print("Output: GPA 4.0")
    case voto if voto >= 101 and voto <= 105:
        print("Output 3.7")
    case voto if voto >= 96 and voto <= 100:
        print("Output 3.3")
    case voto if voto >= 91 and voto <= 95:
        print("Output 3.0")
    case voto if voto >= 86 and voto <= 90:
        print("Output 2.7")
    case voto if voto >= 81 and voto <= 85:
        print("Output 2.3")
    case voto if voto >= 76 and voto <= 80:
        print("Output 2.0")
    case voto if voto >= 70 and voto <= 75:
        print("Output 1.7")
    case voto if voto >= 66 and voto <= 69:
        print("Output 1.0")
    case _:
        print("Voto non valido")
