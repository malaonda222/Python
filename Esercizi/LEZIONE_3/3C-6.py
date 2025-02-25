# chiedere all'utente di inserire il nome di un animale
animale = input("Digita il nome di un animale: ")
habitat = input("Digita l'habitat in cui vive l'animale: ")

# definire le categorie degli animali
Mammiferi = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
Rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
Uccelli = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
Pesci = ["squalo", "trota", "salmone", "carpa"]

# definire categorie di habitat
acqua = "acqua"
aria = "aria"
terra = "terra"

# match statement
match animale:
    case animale if animale in Mammiferi:
        print(f"Output: {animale} appartiene alla categia dei Mammiferi!")
        animal_type = {"animale": animale, "categoria": "Mammiferi"}
    case animale if animale in Rettili:
        print(f"Output: {animale} appartiene alla categia dei Rettili!")
        animal_type = {"animale": animale, "categoria": "Rettili"}
    case animale if animale in Uccelli:
        print(f"Output: {animale} appartiene alla categia dei Uccelli!")
        animal_type = {"animale": animale, "categoria": "Uccelli"}
    case animale if animale in Pesci:
        print(f"Output: {animale} appartiene alla categia dei Pesci!")
        animal_type = {"animale": animale, "categoria": "Pesci"}
    case _:
        print("Il programma non è in grado di classificare l'animale inserito.")
        animal_type = "Unknown"

dizionario = {"animale": name, "animal_type": animal_type, "habitat": habitat}

match (animal_type, habitat):
    case  
        print("L'animale può vivere nell'habitat specificato")
    case 
        print("Avviso: L'habitat non è compatibile con l'habitat specificato")
    case _:
        print("Errore. Animale o habitat non riconosciuti.")