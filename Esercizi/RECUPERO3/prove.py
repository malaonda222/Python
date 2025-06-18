def cambia_lettere(nome: str):
    name = ""
    indice = 0
    for element in nome:
        if indice % 2 == 0:
            name += element.lower()
        else:
            name += element.upper()
        indice += 1
    return f"Mostro: {name}"

nome = "Lisa"
print(cambia_lettere(nome))
