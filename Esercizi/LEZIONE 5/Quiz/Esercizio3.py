def find_disappeared_numbers(nums: list[int]) -> list[int]:
    lista_ordinata_numeri_non_presenti = []
    lista_numeri = len(nums)
    
    for item in range(1, lista_numeri+1):
        if item not in nums:
            lista_ordinata_numeri_non_presenti.append(item)
    
    return lista_ordinata_numeri_non_presenti

nums = [3, 7, 1, 2, 2, 5, 5]
print(find_disappeared_numbers(nums))