# Classifica delle vendite
nome:str = input("Inserisci un nome: ")
vendita:str = input("Inserisci una vendita: ")

max_nome = nome
max_vendita = vendita 
min_nome = nome
min_vendita = vendita 
cont = 0

for cont in range(19):
    new_nome = input("Inserisci un nome del venditore: ")
    new_vendita = float(input("Inserisci il numero di vendite: "))
    if new_vendita > max_vendita:
        max_nome = new_nome
        max_vendita = new_vendita
    if new_vendita < min_vendita:
        max_nome = new_nome
        max_vendita = new_vendita 

print(f"Il venditore che ha avuto più successo è stato {max_nome} con una vendita {max_vendita}")
print(f"Il venditore che ha avuto meno successo è stato {min_nome} con una vendita {min_vendita}")
