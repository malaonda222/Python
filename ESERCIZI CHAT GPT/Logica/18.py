def bilanciate(stringa: str) -> bool:
    contatore = 0
    for element in stringa:
        if element == "(":
            contatore += 1
        if element == ")":
            contatore -= 1 
            if contatore < 0:
                return False 
    
    if contatore == 0:
        return True 
    else:
        return False 
    
print(bilanciate("()()"))
print(bilanciate("(()())"))
print(bilanciate("())("))