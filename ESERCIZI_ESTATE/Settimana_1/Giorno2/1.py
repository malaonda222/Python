'''Scrivi una funzione che verifica se una stringa è palindroma.'''

def palindromo(s: str) -> bool:
    if s == s[::-1]:
        return True 
    else:
        return False
        
print(palindromo("anna"))
print(palindromo("radar"))
print(palindromo("bicicletta"))
print(palindromo("peep"))



def is_palindromo(stringa2: str) -> bool:
    return stringa2 == stringa2[::-1]

print(is_palindromo("Ciao mondo"))
print(is_palindromo("roor"))