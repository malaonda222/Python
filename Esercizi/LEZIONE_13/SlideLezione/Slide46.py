def recursiveSumInRange(a:int, b:int) -> int:
    if a > b:
        temp:int = a #swap
        a = b
        b = temp 
        # a, b = b, a
    if b == a:
        return int(a)
    else:
        return int(b + recursiveSumInRange(a, b-1))
        
print(recursiveSumInRange(5, 10))
print(recursiveSumInRange(10, 5))

