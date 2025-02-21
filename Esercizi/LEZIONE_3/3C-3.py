# creare una lista vuota
oggetti = []
for x in range(3):
    oggetti.append(input("Inserire 3 oggetti della stessa categoria: "))
    print(oggetti)

# match statement
match oggetti:
    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case ["pane", "latte", "uova"]:
        print("prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    case ["telefono", "computer", "tablet"]:
        print("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")

