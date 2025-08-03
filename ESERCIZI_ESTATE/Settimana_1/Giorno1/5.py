''' Unisci due dizionari (secondo sovrascrive primo)'''

def unisci_dizionari(dizionario1: dict[str, int], dizionario2: dict[str, int]) -> dict:
    nuovo_dict = dizionario2|dizionario1
    return nuovo_dict


dizionario1: dict = {"ciao": 2, "come": 3, "va": 4}
dizionario2: dict = {"ciao": 4, "giorno": 4, "notte": 5}

print(unisci_dizionari(dizionario1, dizionario2))