'''Calcolo della Deviazione Standard'''

def calculate_st_dev(nums: list[float]) -> float:
    if not nums:
        raise ValueError("Lista vuota")
    else:
        somma_numeri = 0.0
        for num in nums:
            somma_numeri += num 
        media = somma_numeri / len(nums)

        somma_totale = 0.0
        for num in nums:
            differenza = num - media 
            risultato = differenza ** 2
            somma_totale += risultato 
        risultato_finale_dev_std = somma_totale / len(nums)
        return risultato_finale_dev_std ** 0.5
    
    