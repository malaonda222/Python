# Nome ed età
def utente(name:str, age:int):
    print(f"Il nome dell'utente è {name} e ha {age} anni.")

utente("Emma", 46)

def nome_cognome(name:str, età:int):
    nome = name 
    age = età
    return name, età 

nome, età = nome_cognome("Lisa", 26)
print(nome, età)

