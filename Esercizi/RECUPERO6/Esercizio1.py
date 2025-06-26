def recursivePalindrome(stringa: str) -> bool:
    normalizzata = stringa.replace(" ", "").lower()
    if normalizzata == "":
        return True
    if len(normalizzata) <= 1:
         return True  
    if normalizzata[0] != normalizzata[-1]:
        return False  
    else:
        return recursivePalindrome(normalizzata[1:-1])

print(recursivePalindrome("radar"))
print(recursivePalindrome("Anna"))
print(recursivePalindrome("I topi non avevano nipoti"))
print(recursivePalindrome("casa"))
print(recursivePalindrome("Marta"))
print(recursivePalindrome("Roma e Amore"))

