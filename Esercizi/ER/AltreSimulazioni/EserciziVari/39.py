'''Scrivi una funzione chiamata rotate_list che prenda una lista di 
numeri e un intero k, e restituisca una nuova lista in cui gli elementi 
sono ruotati di k posizioni verso destra. Se k è negativo, la rotazione 
avverrà verso sinistra.

Input:
Una lista di numeri interi nums.
Un intero k che rappresenta il numero di posizioni di rotazione.

Output:
Una nuova lista in cui gli elementi sono ruotati di k posizioni.'''

def rotate_list(nums: list[int], k: int) -> list[int]:
    nuova_lista: list[int] = []
    
    if not nums:
        return "Errore, lista vuota"
    
    k = k % len(nums)
    if k < 0: 
        k += len(nums)
        return nums[-k:] + nums[:-k]
    else:
        return nums 
    

nums = []
k = 3
result = rotate_list(nums, k)
print(result) 

nums = [1, 2, 3, 4, 5]
k = 0
result = rotate_list(nums, k)
print(result)

nums = [1, 2, 3, 4, 5]
k = -2
result = rotate_list(nums, k)
print(result) 

nums = [1, 2, 3, 4, 5]
k = 7
result = rotate_list(nums, k)
print(result) 