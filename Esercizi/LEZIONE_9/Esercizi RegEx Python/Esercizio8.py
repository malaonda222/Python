import re 

def find_codes(text):
    result = re.findall(r'[A-Z0-9]{8}', text)
    return result 

text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
print(find_codes(text))