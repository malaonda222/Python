def recursiveProduttoria(n:int) -> int:
    if n == 0:
        return (0 + 2)
    else:
        return int((n + 2) * recursiveProduttoria(n-1))

print(recursiveProduttoria(7))
    
