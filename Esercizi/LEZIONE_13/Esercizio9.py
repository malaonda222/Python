'''Si scriva una funzione ricorsiva vowelRemover che elimini tutte le vocali da una stringa data e restituisca sotto forma di una nuova stringa la stringa originale ma senza le vocali.

Suggerimento: utilizzare l'operatore + per realizzare la concatenazione di stringhe al fine di costruire la stringa da restituire.'''

# def vowelRemover(my_string:int) -> str:
#     if not my_string:
#         return ""
#     else: 
#         if my_string[0] not in "aeiou":
#             return my_string[0] + vowelRemover(my_string[1:])
#         else:
#             return vowelRemover(my_string[1:])
    
# print(vowelRemover("cielo"))
# print(vowelRemover("chiarissimo"))





# def vowelRemover(my_string:str) -> str:
#     if my_string == "":
#         return ""
#     else:
#         if my_string[-1] in "aeiou":
#             return vowelRemover(my_string[:-1])
#         else:
#             return my_string[-1] + vowelRemover(my_string[:-1])
    
# print(vowelRemover("buongiorno"))




# def vowelRemover(my_string:str) -> str:
#     if my_string == "":
#         return ""
#     else:
#         if my_string[0] not in "aeiou":
#             return my_string[0] + vowelRemover(my_string[1:])
#         else:
#             return vowelRemover(my_string[1:])
        
# print(vowelRemover("bellissimo"))


# def vowelRemover(stringa1:str) -> str:
#     if stringa1 == "":
#         return ""
#     else:
#         if stringa1[0] in "aeiou":
#             return vowelRemover(stringa1[1:])
#         else:
#             return stringa1[0] + vowelRemover(stringa1[1:])




def vowelRemover(my_string:str) -> str:
    if not my_string:
        return ""
    if my_string[0].lower() not in ["a", "e", "i", "o", "u"]:
        return my_string[0] + vowelRemover(my_string[1:])
    else:
        return "" + vowelRemover(my_string[1:])
    
print(vowelRemover("idolo"))