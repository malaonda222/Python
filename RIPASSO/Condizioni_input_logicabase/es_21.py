'''
Traccia:
Scrivi una funzione divisibili_tre_cinque() -> None che:
* Scorra i numeri da 1 a 100 (inclusi).
* Per ciascun numero, verifichi se è divisibile sia per 3 che per 5.
* Se lo è, lo stampi a video.
'''

def divisibili_tre_cinque() -> None:
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(i)
        else:
            continue

divisibili_tre_cinque()