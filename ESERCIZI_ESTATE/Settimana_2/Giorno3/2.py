'''Elimina parole duplicate da una lista usando set comprehension.'''

testo: list = ["mangiare", "bere", "dormire", "mangiare", "tutto", "a", "pranzo", "e", "a", "cena"]
parole_uniche = {element for element in testo}
print(parole_uniche)

