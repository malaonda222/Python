'''In una lista, tutti gli elementi compaiono due volte, tranne uno. Scrivi una funzione
find_unique(lst) che trova quell’elemento senza usare dizionari o contatori.'''

def find_unique(lst: list) -> int:
    for element in lst:
        if lst.count(element) == 1:
            print(element)
        

find_unique([4, 3, 2, 4, 2, 3, 7])