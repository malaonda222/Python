from string import ascii_lowercase, ascii_uppercase

def caesar_cypher_encrypt(s: str, key: int) -> str:
    if key < 0 or key % 1 != 0: 
        raise ValueError("La chiave deve essere un numero intero positivo.")
    else:
        s_criptata = ""
        for element in s:
            if element in ascii_lowercase:
                indice = ascii_lowercase.index(element)
                nuovo_indice = (indice + key) % 26
                lettera_criptata = ascii_lowercase[nuovo_indice]
                s_criptata += lettera_criptata
            elif element in ascii_uppercase:
                indice = ascii_uppercase.index(element)
                nuovo_indice = (indice + key) % 26
                lettera_criptata = ascii_lowercase[nuovo_indice]
                s_criptata += lettera_criptata
            else:
                s_criptata += element
        return s_criptata 

def caesar_cypher_decrypt(s: str, key: int) -> str:
    if key < 0 or key % 1 != 0:
        raise ValueError("La chiave deve essere un numero intero positivo.")
    else:
        s_decriptata = ""
        for element in s:
            if element in ascii_lowercase:
                indice = ascii_lowercase.index(element)
                nuovo_indice = (indice - key) % 26
                lettera_decriptata = ascii_lowercase[nuovo_indice]
                s_decriptata += lettera_decriptata
            elif element in ascii_uppercase:
                indice = ascii_uppercase.index(element)
                nuovo_indice = (indice - key) % 26
                lettera_decriptata = ascii_uppercase[nuovo_indice]
                s_decriptata += lettera_decriptata
            else:
                s_decriptata += element 
        return s_decriptata



print(caesar_cypher_encrypt("si ciaz", 2))
print(caesar_cypher_decrypt("si ciaz", 2))
print(-3 % 26)


def crittografia(s: str, key: int) -> str:
    if key < 0 or type(key) != int:
        raise ValueError("la chiave deve essere un numero intero maggiore di 0.")
    else:
        stringa_crittografata = ""
        for element in s:
            if element in ascii_lowercase:
                indice_lettera = ascii_lowercase.index(element)
                nuovo_indice = (indice_lettera + key) % 26
                lettera_criptata = ascii_lowercase[nuovo_indice]
                stringa_crittografata += lettera_criptata
            elif element in ascii_uppercase:
                indice_lettera = ascii_uppercase.index(element)
                nuovo_indice = (indice_lettera + key) % 26
                lettera_criptata = ascii_uppercase[nuovo_indice]
                stringa_crittografata += element
            else:
                stringa_crittografata += element
        return stringa_crittografata 

def decrittografia(s: str, key: int) -> str:
    if key < 0 or type(key) != int:
        raise ValueError("La chiave non può essere un numero minore di zero e deve essere un intero.")
    else:
        stringa_decrittografata = ""
        for element in s:
            if element in ascii_lowercase:
                indice_lettera = ascii_lowercase.index(element)
                nuovo_indice = (indice_lettera - key) % 26
                indice_lettera = ascii_lowercase[nuovo_indice]
                stringa_decrittografata += indice_lettera
            if element in ascii_uppercase:
                indice_lettera = ascii_uppercase.index(element)
                nuovo_indice = (indice_lettera - key) % 26
                indice_lettera = ascii_uppercase[nuovo_indice]
                stringa_decrittografata += indice_lettera
            else:
                stringa_decrittografata += element
        return stringa_decrittografata
    

