def transform(x: int) -> int:
    if x % 2 == 0:
        return x / 2
    else:
        return (x * 3) - 1 
    
print(transform(4))
print(transform(-10))