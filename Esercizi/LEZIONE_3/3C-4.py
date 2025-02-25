# chiedere all'utente di inserire il nome di un animale
animale = input("Digita il nome di un animale: ")

# definire le categorie degli animali
Mammiferi = ["cane", "gatto", "cavallo", "elefante", "leone"]
Rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
Uccelli = ["aquila", "pappagallo", "gufo", "falco"]
Pesci = ["squalo", "trota", "salmone", "carpa"]

# match statement
match animale:
    case animale if animale in Mammiferi:
        print(f"Output: {animale} appartiene alla categia dei Mammiferi!")
    case animale if animale in Rettili:
        print(f"Output: {animale} appartiene alla categia dei Rettili!")
    case animale if animale in Uccelli:
        print(f"Output: {animale} appartiene alla categia dei Uccelli!")
    case animale if animale in Pesci:
        print(f"Output: {animale} appartiene alla categia dei Pesci!")
    case _:
        print("Il programma non è in grado di classificare l'animale inserito.")
