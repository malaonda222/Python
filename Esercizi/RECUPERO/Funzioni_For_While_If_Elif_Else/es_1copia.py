def combinazione(x: bool, y: bool, z: bool) -> bool:
    if x == True and (y == True or z == True):
        return "Azione permessa"
    else:
        return "Azione negata"
    

def combinazione1(x: bool, y: bool, z: bool) -> bool:
    if not x == False and (not y == False or z == True):
        return "Azione permessa"
    else:
        return "Azione negata"


print(combinazione(True, False, True))
print(combinazione1(False, False, True))