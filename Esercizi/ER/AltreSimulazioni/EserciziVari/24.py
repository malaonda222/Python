'''Format Emails
Descrizione:
Scrivi una funzione chiamata format_emails che riceve in ingresso una lista di dizionari. 
Ogni dizionario rappresenta un utente e contiene le chiavi "nome" e "email".

La funzione deve restituire una singola stringa dove ogni elemento è formattato come: nome <email>
Gli elementi devono essere separati da una virgola.

Formato lista:
[
    {"nome": "Anna", "email": "anna@example.com"},
    {"nome": "Marco", "email": "marco@example.com"}
]
'''

def format_emails(users: list[dict[str, str]]) -> str:
    nuova_lista = []
    for user in users:
        nome = user["nome"]
        email = user["email"]
        nuova_lista.append(f"{nome} <{email}>")
    return ",".join(nuova_lista)

print(format_emails([{"nome": "Anna", "email": "anna@example.com"},
    {"nome": "Marco", "email": "marco@example.com"}]))