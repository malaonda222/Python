# chiedere all'utente di inserire le coordinate di un punto
x = int(input("Inserisci la coordinata \"x\": "))
y = int(input("Inserisci la coordinata \"y\": "))

# match statement
point = (x, y)
match point:
    case (0, 0):
        print("Il punto si trova nell'origine")
    case (x, 0):
        print("Il punto  si trova sull'asse X")
    case (0, y):
        print("Il punto si trova sull'asse Y")
    case point if x > 0 and y > 0:
        print("Il punto si trova nel primo quadrante")
    case point if x < 0 and y > 0:
        print("Il punto si trova nel secondo quadrante")
    case point if x < 0 and y < 0:
        print("Il punot si trova nel terzo quadrante")
    case point if x > 0 and y < 0:
        print("Il punto si trova nel quarto quadrante")