import re 

def find_dates(text):
    pattern = (r'\b(?:0[1-9]|[12][0-9]|3[01])/(?:0[1-9]|1[0-2])/(?:19|20)\d{2}\b')
    return re.findall(pattern, text)

text = "Le date importanti sono 09/04/2025 e 15/08/2023."
print(find_dates(text))