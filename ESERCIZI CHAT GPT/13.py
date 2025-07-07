def anagramma(stringa1: str, stringa2: str) -> bool:
    if sorted(stringa1) == sorted(stringa2) and len(stringa1) == len(stringa2):
        return True
    else:
        return False 
    

print(anagramma("roma", "amor"))
print(anagramma("ciao", "caio"))