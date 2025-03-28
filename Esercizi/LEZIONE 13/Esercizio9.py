def vowelRemover(my_string:int) -> str:
    if not my_string:
        return ""
    else: 
        if my_string[0] not in "aeiou":
            return my_string[0] + vowelRemover(my_string[1:])
        else:
            return vowelRemover(my_string[1:])
    
print(vowelRemover("cielo"))
print(vowelRemover("chiarissimo"))