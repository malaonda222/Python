# chiedere all'utente di inserire una frase 
stringa = input("Inserisci una frase: ")

#match statement
lunghezza = len(stringa)
match stringa:
    case stringa if stringa[-1] == "?" and lunghezza % 2 == 0:
        print("Sì")
    case stringa if stringa[-1] == "?" and lunghezza % 2 != 0:
        print("No")
    case stringa if stringa[-1] == "!":
        print("Wow!")
    case _:
        print(f"Tu dici {stringa}")


