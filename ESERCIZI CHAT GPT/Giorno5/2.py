def is_palindrome(stringa: str) -> bool:
    stringa_pulita = stringa.replace(" ", "").lower()
    return stringa_pulita == stringa_pulita[::-1]

frase = "I topi non avevano nipoti"
print(is_palindrome(frase))
