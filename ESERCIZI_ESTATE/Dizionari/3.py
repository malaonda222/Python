'''diz = {"a": 1, "b": 2, "c": 3}
valore diventi chiave e la chiave il valore'''

def cambia_ordine(dizionario: dict[str, int]) -> dict[int, str]:
    return {value: key for key, value in dizionario.items()}

print(cambia_ordine({"a": 1, "b": 2, "c": 3}))