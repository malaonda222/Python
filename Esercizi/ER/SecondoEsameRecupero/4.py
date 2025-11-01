def calculate_std_dev(nums: list[float]) -> float:
    if not nums: 
        raise ValueError("Lista vuota")
    else:
        somma = 0.0
        conteggio = 0.0
        for num in nums:
            somma += num 
            conteggio += 1
        media = somma / conteggio 
        
        varianza_numeri = 0.0
        for num in nums:
            varianza_numeri += (num-media)**2
        result = varianza_numeri/conteggio 
        return result ** 0.5
    
print(calculate_std_dev([1.0, 2.0, 3.0, 4.0, 5.0]))


def calculate_std_dev(nums: list[float]) -> float:
    if not nums:
        raise ValueError("Lista vuota")
    
    media = sum(nums)/len(nums)
    varianza = 0
    for num in nums:
        varianza += (num-media)**2
    result = varianza / len(nums) 
    return result**0.5 


def calculate_std_dev(nums: list[float]) -> float:
    if not nums:
        raise ValueError("lista vuota")
    else:
        somma = 0.0
        for num in nums:
            somma += num 
        media = somma / len(nums)

        somma_varianza = 0.0
        for num in nums:
            differenza = (num - media) ** 2
            somma_varianza += differenza 
        media_varianza = somma_varianza / len(nums)
        return media_varianza ** 0.5
    

