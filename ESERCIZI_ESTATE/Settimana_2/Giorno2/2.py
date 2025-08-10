'''Crea una lista di lunghezze di parole da una frase.'''

lista_stringhe = ["ciao", "ragazzi", "come", "va"]
lunghezza_stringhe = [len(element) for element in lista_stringhe]
print(lunghezza_stringhe)


stringa = "ciao ragazzi come va"
lunghezze = {parola: len(parola) for parola in stringa.split()}
print(lunghezze)