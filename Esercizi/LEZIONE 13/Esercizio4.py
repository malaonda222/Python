def recursiveDigitCounter(n:int) -> int:
    if n >= -9 and n <= 9:
        return 1
    else:
        return int(1 + recursiveDigitCounter(n // 10))


print(recursiveDigitCounter(12345))
print(recursiveDigitCounter(1587365))

