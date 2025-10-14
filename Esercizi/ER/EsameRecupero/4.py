def calculate_stats(nums: list[float]) -> dict[str, float]:
    if nums == []:
        raise ValueError("Errore. Lista vuota")

    minimo = nums[0]
    massimo = nums[0]
    somma = 0.0
    conteggio = 0
    for num in nums:
        if num < minimo:
            minimo = num 
        if num > massimo:
            massimo = num 
        somma += num
        conteggio += 1

    avg = somma/conteggio
    return {"min": minimo, "max": massimo, "avg": avg}



print(calculate_stats([1, 6, 2, 3, 11]))


def calculate_stats(nums: list[float]) -> dict[str, float]:
    if nums == []:
        raise ValueError("Errore. Lista vuota.")
    
    minimo = nums[0]
    massimo = nums[0]
    for num in nums:
        if num < minimo:
            minimo = num 
        if num > massimo:
            massimo = num 
    
    avg = sum(nums)/len(nums)
    return {"min": minimo, "max": massimo, "avg": avg}

print(calculate_stats([1, 6, 2, 3, 22]))