def recursivePower(base:int, exponent:int) -> None:
    
    # if base == 0: non è necessrio
    #     return 0
    if exponent == 0:
        return 1
    elif base == 0 and exponent == 0:
        return 0
    else:
        return int(base * recursivePower(base, exponent-1))

print(recursivePower(3, 4))
print(recursivePower(4, 3))
print(recursivePower(2, 5))
print(recursivePower(5, 2))

