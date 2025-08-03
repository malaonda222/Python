'''Inverti le parole in una frase: "ciao mondo" → "mondo ciao".'''

def inverti_parole(stringa1: str) -> str:
    tokens = stringa1.split()
    nuova_stringa = ""
    for token in tokens[::-1]:
        nuova_stringa += " " + token
    return nuova_stringa

print(inverti_parole("ciao mondo"))


def inverti_parole2(stringa2: str) -> str:
    tokens = stringa2.split()
    return " ".join(tokens[::-1])

print(inverti_parole2("ciao mondo"))

parole = ["ciao", "mondo", "come", "va", "?"]
frase = " ".join(parole)
print(frase)


def inverti_parole2(stringa2: list[str]) -> str:
    tokens = stringa2.split()
    return " ".join(tokens[::-1])

print(inverti_parole2("ciao mondo"))