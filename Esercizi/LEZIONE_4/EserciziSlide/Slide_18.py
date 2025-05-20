# Funzioni con più valori (tuple, liste o dizionari)

def operations(a:int, b:int) -> tuple[int, int]:
    sum_result:int = a+b 
    diff_result:int = a-b 
    return sum_result, diff_result

sum_value, diff_value = operations(10, 5)
print("Sum:", sum_value)
print("Difference", diff_value)