def recursiveProduttoria(n:int) -> int:
    if n == 1:
        return 1**3
    else:
        return (int(n**3) * recursiveProduttoria(n - 1))

print(recursiveProduttoria(3))