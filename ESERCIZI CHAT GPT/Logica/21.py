def palindromo(n: int) -> bool:
    s = str(n)
    if s == s[::-1]:
        return True 
    else:
        return False 
    

print(palindromo(121)) 