def bubble_sort(lista: list[int]) -> list[int]:
    n = len(lista)
    for i in range(n):
        scambio = False 
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                scambio = True 
        
        if scambio == False:
            break 
        