def is_palindroma(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return is_palindroma(s[1:-1])
    
print(is_palindroma("radar"))
print(is_palindroma("ciao"))
