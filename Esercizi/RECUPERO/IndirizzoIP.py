def is_valid_ip4(address: str) -> bool:
    tokens = address.split(".")
    if len(tokens) != 4:
        return False
    for token in tokens:
        if not token.isdigit():
            return False
        num = int(token)
        if num < 0 and num > 256:
            return False
    return True 
     

indirizzo = is_valid_ip4("192.168.0.1")
indirizzo2 = is_valid_ip4("255.255.255.255")
indirizzo3 = is_valid_ip4("256.100.10.1")
indirizzo4 = is_valid_ip4("192.168.1")
indirizzo5 = is_valid_ip4("192.168.1.a")

print(indirizzo)
print(indirizzo2)
print(indirizzo3)
print(indirizzo4)
print(indirizzo5)






#4 numeri decimali (da 0 a 255) separati da 3 punti
#se non ci sono 3 punti o 4 parti numeriche resituisci False 
#ciascuna parte deve contenere solo (isdigit()) e convertita in intero deve essere nel range [0,255][0,225][0,225]
#non deve contenere caratteri o spazi aggiuntivi