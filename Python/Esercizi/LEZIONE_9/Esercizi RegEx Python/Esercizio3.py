import re 

def mask_numbers(text):
    result = re.sub(r'\d+', '###', text)
    return result

text = "Il codice è 12345 e la data è 2025."
frase_nuova = mask_numbers(text)
print(frase_nuova)