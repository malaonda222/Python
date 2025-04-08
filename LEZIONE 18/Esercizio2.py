import string

def validate_password(password:str) -> bool:
    
    if len(password) < 20:
        raise ValueError("La password deve essere lunga almeno 20 caratteri.")
    
    count_maiuscole = 0
    for item in password:
        if item.upper():
            count_maiuscole += 1
    if count_maiuscole < 3:
        raise ValueError("La password deve avere almeno tre lettere maiuscole.")
    
    count_speciali = 0
    for item in password:
        if item in string.punctuation:
            count_speciali += 1
    if count_speciali < 4:
        raise ValueError("La password deve avere almeno quattro caratteri speciali.")

    return True

print(validate_password("LisaBandinelliO98?!=?"))
print(validate_password("fuffi?!=?"))


try:
    password = "Abc#@123"
    print(validate_password(password))
except ValueError as e:
    print(f"Errore: {e}")
