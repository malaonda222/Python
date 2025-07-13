def is_primo(n:int) -> bool:
    if n < 2:
        return False 
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True 

def filtra_primi(lista: list[int]) -> list[int]:
    return [n for n in lista if is_primo(n)]


print(filtra_primi([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(filtra_primi([1, 5, 18, 22]))