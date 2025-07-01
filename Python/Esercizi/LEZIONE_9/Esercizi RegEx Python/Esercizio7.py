import re

def is_valid_name(name):
    result = re.match(r'^[A-Z]{1}[a-z]{2,}$', name)
    return bool(result)

name:str = "Marco"
print(is_valid_name(name))
name:str = "marco"
print(is_valid_name(name))
name:str = "Ma"
print(is_valid_name(name))