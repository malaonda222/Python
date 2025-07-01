def mostra_info(persona):
    print(f"Nome: {persona['nome']}")
    print(f"Cognome: {persona['cognome']}")
    print(f"Età: {persona['età']}")

persona1 = {
    'nome': "Lisa",
    'cognome': "Bandinelli",
    'età': 26
}

mostra_info(persona1)



def mostra_nomi(animale):
    print(f"Colore: {animale['colore']}")
    print(f"Città: {animale['città']}")
    print(f"Carattere: {animale['carattere']}")

animale1 = {
    'colore': "nero",
    'città': "Roma",
    'carattere': "tranquillo"
}

mostra_nomi(animale1)
