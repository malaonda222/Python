def verifica_condizioni(x: bool, y: bool, z: bool) -> str:
    if x == True and (y == True or z == True):
        return "Azione permessa"
    else:
        return "Azione negata"
    
print(verifica_condizioni(True, False, False))
