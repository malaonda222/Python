def recursive_frase(s: str) -> str:
    if s == "":
        return ""
    return s[-1] + recursive_frase(s[:-1])
    

print(recursive_frase("ciao"))