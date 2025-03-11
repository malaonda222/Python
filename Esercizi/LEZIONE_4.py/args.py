mylist = [1, 2, 3, 4, 5]
print(mylist)

print(*mylist)

def nome_funzione(*args, **kwards) -> None:
    print(args, kwards)

nome_funzione("valore1", "valore2", chiave1 = "valore1")



def nome_funzione(x, y, *args, **kwargs) -> None:
    for key, value in kwargs.items():
        if key == "chiave1":
            print(value)
        elif key == "chiave2":
            print(value)
        else:
            raise ValueError("Chiave non riconosciuta"):
        print("Parametro non riconosciuto")

nome_funzione("valore1", "valore2", chiave1 = "valore1")



