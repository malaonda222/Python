import re 

def check_product_code(code):
    pattern = (r'^[A-Z]{4}-\d{4}-[A-Z]{2}$')
    return bool(re.fullmatch(pattern, code))

print(check_product_code("PROD-9876-ZX"))  
print(check_product_code("PROD-99-ZX"))