def charDuplicator(my_string:str) -> str:
    if not my_string:
        return ""
    else:
        return my_string[0] * 2 + charDuplicator(my_string[1:])

print(charDuplicator("libro"))
print(charDuplicator("Arcobaleno"))