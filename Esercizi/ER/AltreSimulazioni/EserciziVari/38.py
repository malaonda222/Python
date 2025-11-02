'''Scrivi una funzione chiamata find_max_min che prenda una lista di 
numeri interi e restituisca una tupla con il valore massimo e il 
valore minimo della lista.
Input:
Una lista di numeri interi nums.

Output:
Una tupla con due valori: il primo è il massimo, il secondo è il minimo. 
Se la lista è vuota, restituisci una tupla (None, None).'''

def find_max_min(nums: list[int]) -> tuple[int, int]:
    if not nums:
        return (None, None)
    
    valore_max = nums[0]
    valore_min = nums[0]
    
    for num in nums:
        if num > valore_max or valore_max == None:
            valore_max = num 
        if num < valore_min or valore_min == None:
            valore_min = num 

    else:
        return (valore_max, valore_min)
    

print(find_max_min([]))
print(find_max_min([22, 5, 66, 47, 3333, 0]))


