import re

def extract_emails(text):
    result = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
    return result

text = "Contattaci a info@azienda.com oppure support@help.org"
email_trovate = extract_emails(text)
print(email_trovate)