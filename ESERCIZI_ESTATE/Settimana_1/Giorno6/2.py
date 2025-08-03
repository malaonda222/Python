'''Usa break per fermare un ciclo se un elemento è trovato.'''

lista_elementi: list = ["Lisa", 5, True, 0.9, "ciao"]
trovato = False 
elemento_da_trovare = 9

for element in lista_elementi:
    if element == elemento_da_trovare:
        trovato = True 
        print(f"Elemento '{element}' presente nella lista")
        break  
if trovato == False:
    print(f"Elemento '{elemento_da_trovare}' non presente nella lista")
    