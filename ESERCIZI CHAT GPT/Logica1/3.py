def sequenza_alternata(sequenza: list[int]) -> bool:
    for i in range(len(sequenza) - 1):
        if sequenza[i] % 2 == 0:
            if sequenza[i + 1] % 2 == 0:
                return False 
            else:
                continue 
        if sequenza[i] % 2 == 1:
            if sequenza[i + 1] % 2 == 1:
                return False 
            else:
                continue 
    return True 


def sequenza_alternata1(sequenza: list[int]) -> bool:
    for i in range(len(sequenza) - 1):
        if sequenza[i] % 2 == sequenza[i + 1] % 2:
            return False 
    return True


print(sequenza_alternata([2, 3, 4, 5, 6]))
print(sequenza_alternata([1, 2, 3, 4, 5]))
print(sequenza_alternata([1, 1, 2, 4]))