'''Logica: Data una parola, genera tutte le sue permutazioni possibili.'''

def permutazioni(stringa: str) -> list[str]:
    if not stringa:
        return []
    perm = [stringa[0]]
    for lettera in stringa[1:]:
        nuove_perm = []
        for element in perm:
            for i in range(len(element) + 1):
                nuova = element[:i] + lettera + element[i:]
                nuove_perm.append(nuova)
        perm = nuove_perm
    return perm 


print(permutazioni("abc"))