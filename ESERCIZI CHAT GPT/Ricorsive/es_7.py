def recursive_frase(s: str) -> str:
    if s == "":
        return ""
    return s[-1] + recursive_frase(s[:-1])
    

print(recursive_frase("ciao"))
print(recursive_frase("precipitosamente andai"))




def inverti_parola(parola: str) -> str:
    if len(parola) <= 1:
        return parola 
    else:
        return inverti_parola(parola[1:]) + parola[0]
    
print(inverti_parola("Come va?"))