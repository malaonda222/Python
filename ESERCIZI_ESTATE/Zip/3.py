'''Usa zip() per combinare numeri.
Usa zip() per creare una nuova lista con la somma degli elementi 
corrispondenti.
Output atteso: [11, 22, 33]'''

lista1 = [10, 20, 30]
lista2 = [1, 2, 3]
nuova_lista = zip(lista1 + lista2)
print(nuova_lista)