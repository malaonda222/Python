def nomi():
    i = 0
    lista_nomi = []

    while i <= 30:
        nome = input("Inserire il nome di una persona: ").strip().title()
        if nome in lista_nomi:
            print("Nome già inserito")
            break 
        if len(nome) > 20:
            print("Errore. Il nome deve essere lungo max 20 caratteri!")
            continue
        if nome == "":
            print("Errore. Il nome non può essere vuoto.")
        else:
            lista_nomi.append(nome)
            i += 1

    print(f"Lista dei nomi inseriti: {lista_nomi}")

    print(f"Hai inserito {len(lista_nomi)} nomi distinti")

    max_nome = lista_nomi[0]
    for nome in lista_nomi:
        if len(nome) > len(max_nome):
            max_nome = nome 
    print(f"Il nome più lungo della lista è {max_nome} con {len(max_nome)} caratteri")
nomi()