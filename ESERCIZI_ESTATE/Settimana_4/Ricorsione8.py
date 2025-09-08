def permutazioni(s: str) -> list[str]:
    if len(s) == 1:
        return list(s) 
    risultato = []
    for i in range(len(s)):
        c = s[i]
        resto = s[:i] + s[i+1:]
        sottopermutazioni = permutazioni(resto)
        for perm in sottopermutazioni:
            risultato.append(c + perm)
    return risultato

print(permutazioni("abc"))
    
