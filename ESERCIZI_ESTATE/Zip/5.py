'''Crea un dizionario da due liste
Partendo da due liste, usa zip() per combinarle e crea un dizionario dove:
Le chiavi sono i nomi degli studenti
I valori sono i rispettivi voti'''

studenti = ['Anna', 'Luca', 'Marco']
voti = [28, 30, 25]

nuova_lista = zip(studenti, voti)

new_dict = {}
for studente, voto in nuova_lista:
    new_dict[studente] = voto 
print(new_dict)