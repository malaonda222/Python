# chiedere all'utente di inserire il nome di un animale
animale = input("Digita il nome di un animale: ").lower()
habitat = input("Digita l'habitat in cui vive l'animale: ").lower()

# definire le categorie degli animali
Mammiferi:list = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
Rettili:list = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
Uccelli:list = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
Pesci:list = ["squalo", "trota", "salmone", "carpa"]

# definire categorie di habitat
habitats:list = ["acqua", "aria", "terra"]

# match statement
match animale:
    case animale if animale in Mammiferi:
        animal_type = "mammiferi"
        print(f"Output: \"{animale}\" appartiene alla categoria dei Mammiferi!")
    case animale if animale in Rettili:
        animal_type = "rettili"
        print(f"Output: \"{animale}\" appartiene alla categoria dei Rettili!")
    case animale if animale in Uccelli:
        animal_type = "uccelli"
        print(f"Output: \"{animale}\" appartiene alla categoria dei Uccelli!")
    case animale if animale in Pesci:
        animal_type = "pesci"
        print(f"Output: \"{animale}\" appartiene alla categoria dei Pesci!")
    case _:
        print("Il programma non è in grado di classificare l'animale inserito.")
        animal_type = "unknown"

#animal_type = ["mammiferi", "rettili", "uccelli", "pesci", "unknown"]
diz:dict[str, str] = {
    "nome": animale, 
    "tipo animale": animal_type, 
    "habitat": habitat
}

match animal_type:
    case animal_type if animal_type == "mammiferi":
        match habitat:
            case habitat if habitat == "terra":
                print(f"L'animale {animale} è uno dei {animal_type} che vive sulla terra")
            case habitat if habitat == "acqua": 
                print(f"L'animale {animale} è uno dei {animal_type} che vive in acqua")
            case _: 
                print("L'habitat non è compatibile con l'habitat specificato")
    case animal_type if animal_type == "rettili":
         match habitat:
            case habitat if habitat == "terra":
                print(f"L'animale {animale} è uno dei {animal_type} che vive sulla terra")
            case habitat if habitat == "acqua": 
                print(f"L'animale {animale} è uno dei {animal_type} che vive in acqua")
            case _:    
                print("L'habitat non è compatibile con l'habitat specificato")
    case animal_type if animal_type == "uccelli":
         match habitat:
            case habitat if habitat == "terra":
                print(f"L'animale {animale} è uno dei {animal_type} che vive sulla terra")
            case habitat if habitat == "aria": 
                print(f"L'animale {animale} è uno dei {animal_type} che vive in aria")
            case _:    
                print("L'habitat non è compatibile con l'habitat specificato")
    case animal_type if animal_type == "pesci":
         match habitat:
            case habitat if habitat == "acqua":
                print(f"L'animale {animale} è uno dei {animal_type} che vive in acqua")
            case _:    
                print("L'habitat non è compatibile con l'habitat specificato")
    case _:
        print("Errore. L'animale o l'habitat non sono riconosciuti.")

    
match diz:
    case {"animale": animale, "animal_type": "mammiferi", "habitat": habitat} if habitat in ["terra", "acqua"]:
        match animale:
                case animale if animale in ["cane", "gatto", "cavallo", "elefante", "leone"] and habitat == "terra":
                    print(f"L'animale {animale} è uno dei mammiferi che può vivere sulla terra!")
                case animale if animale in ["balena", "delfino"] and habitat == "acqua":
                    print(f"L'animale {animale} è uno dei mammiferi che può vivere in acqua!")
                case _:
                    print(f"Non ho mai visto l'animale {animale} vivere nell'habitat {habitat}")
    case {"animale": animale, "animal_type": "uccelli", "habitat": habitat} if habitat in ["terra", "acqua", "aria"]:
        match animale:
                case animale if animale in ["gallina", "tacchino"] and habitat == "terra":
                    print(f"L'animale {animale} è uo degli uccelli che può vivere sulla terra")
                case animale if animale in ["cigno", "anatra"] and habitat ["acqua", "terra"]:
                    print(f"L'animale {animale} è uno degli uccelli che può vivere in aria")  
                case _:
                    print()                       

    case {"animale": animale, "animal_type": "uccelli", "habitat": habitat} if habitat in ["terra", "acqua", "aria"]:
        match habitat:
            case "acqua":
                print(f"L'animale {animale} è uno dei pesci che vive in acqua!")
            case _:
                print(f"Non ho mai visto nessun pesce vivere fuori dall'acqua!")

    case _:
        print(f"Non sono in grado di fornire alcuna informazione per l'animale inserito!")