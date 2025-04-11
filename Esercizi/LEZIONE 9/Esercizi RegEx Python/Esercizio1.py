'''Verifica se una stringa è un numero intero'''
import re 

def is_integer(s:int) -> bool:
    return bool(re.match(r'^-?\d+$', s))

print(is_integer("123"))
print(is_integer("-456"))
print(is_integer("12.3"))
