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
