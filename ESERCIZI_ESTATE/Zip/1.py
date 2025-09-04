'''
Usa zip() per creare una lista di nome completo (es. "Luca Bianchi").
Stampa ogni nome completo su una riga diversa.
'''

nomi = ["Luca", "Anna", "Marco"]
cognomi = ["Bianchi", "Rossi", "Verdi"]
lista_completa = zip(nomi, cognomi)

for nome, cognome in lista_completa:
    print(f"{nome} {cognome}")