def is_palindrome(n: int) -> bool:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Errore. Il numero deve essere un intero positivo.")
    else:
        n_stringa = str(n)
        stringa_invertita = n_stringa[::-1]
        if n_stringa == stringa_invertita:
            return True
        else:
            return False 
        

