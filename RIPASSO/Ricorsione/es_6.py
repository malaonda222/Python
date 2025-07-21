'''Scrivi una funzione ricorsiva palindromo(s) che restituisca True se la 
stringa s è un palindromo, False altrimenti.'''

def is_palidromo(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False 
    else:
        return is_palidromo(s[1:-1])


print(is_palidromo("radar"))
print(is_palidromo("python"))
