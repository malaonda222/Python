def triangolo_valido(x: int, y: int, z: int) -> bool:
    if (x + y) > z and (x + z) > y and (y + z) > x:
        return True 
    else:
        return False 
    
print(triangolo_valido(3, 4, 5))
print(triangolo_valido(1, 1, 3))
