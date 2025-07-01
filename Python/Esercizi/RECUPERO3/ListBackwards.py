# def ListBackwards(lista_backwards: list, indice = None):
#     if lista_backwards == []:
#         print("Errore, lista vuota")
#         return 
#     if indice is None:
#         indice = len(lista_backwards) - 1
#     if indice < 0:
#         return
    
#     print(lista_backwards[indice], end=" ")
#     ListBackwards(lista_backwards, indice - 1)


# lista1: list = [1, 2, 3, 4, 5]
# ListBackwards(lista1)
# print("\n")
# lista2 = []
# ListBackwards(lista2)
# print()
# lista3 = ["Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"]
# ListBackwards(lista3)




def ListBackward(lista_back: list[int|float|str|bool], indice = None) -> list[int|float|str|bool]:
    if not lista_back:
        return []
    if indice is None:
        indice = len(lista_back) - 1
    if indice < 0:
        return []
    
    print(lista_back[indice], end=" ")
    ListBackward(lista_back, indice-1)
    
lista1 = [1, 2, 3, 4]
ListBackward(lista1)














