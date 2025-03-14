def saluto(nome, età=55):
    print(f"Mi chiamo {nome} e ho {età} anni.")

saluto("Mario")
saluto("Maurizio", età=89)
saluto(età=77, nome="Simone")


def credenziali(email:str, password:str):
    print(f"L'email di registrazione è {email} e la password è {password}")

credenziali("bandi@gmail.com", "F98")
credenziali("ele.bandi@gmail.com", "G467")


def animale(animal:str, colore:str):
    print(f"L'animale {animal} è di colore {colore}")

animale("giraffa", "marrone")



