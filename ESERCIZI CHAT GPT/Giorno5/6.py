def lettere_uniche(stringa: str) -> bool:
    viste = set()
    for lettera in stringa:
        if lettera in viste:
            return False
        viste.add(lettera)
    return True
        
print(lettere_uniche("cane"))
print(lettere_uniche("cassa"))
