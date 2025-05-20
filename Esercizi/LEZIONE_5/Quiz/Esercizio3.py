def find_disappeared_numbers(nums: list[int]) -> list[int]:
    lista_ordinata_numeri_non_presenti = []
    lista_numeri = len(nums)
    
    for item in range(1, lista_numeri+1):
        if item not in nums:
            lista_ordinata_numeri_non_presenti.append(item)
    
    return lista_ordinata_numeri_non_presenti

nums = [3, 7, 1, 2, 2, 5, 5]
print(find_disappeared_numbers(nums))

# soluzione Profe
def find_disappeared_numbers(nums: list[int]) -> list[int]:
    n:int = len(nums)
    full_set:set[int] = set(range(1, n + 1))  # Crea un insieme con tutti i numeri da 1 a n
    nums_set:set[int] = set(nums)             # Converte la lista originale in un insieme
    missing:list[int] = list(full_set - nums_set)  # Trova la differenza tra i due insiemi

    return sorted(missing)               # Restituisce i numeri mancanti ordinati

# Test case
print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))  # Output: [5, 6]
