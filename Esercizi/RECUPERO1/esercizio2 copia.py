def isValid(x: int) -> bool:
    return x.is_integer() and x >= 0

def insertValidnumber() -> int:
    while True:
        x = int(input("Inserisci un numero intero positivo: "))
        if isValid(x):
            break 
        else:
            print("Il numero inserito non è valido.")
    return x 

if __name__ == "__main__":
    x: int = insertValidnumber()
    occ: int = 0
    pos: int = 0
    seq: list[int] = []
    somma: int = 0

    print("Digitare sequenza: ")
    while True:
        n: int = insertValidnumber()

        seq.append(n)

        if n == x:
            occ += 1 

        if occ == 1 and n == x:
            pos = seq.index(n)
        
        if n != x:
            somma = somma + n

        if n == 0:
            break  

        print("Hai inserito la sequenza: ", *seq)

        if occ == 1:
            print(f"Il numero {x} compare {occ} volte nella sequenza.")
        else:
            print(f"Il numero {x} compare {occ} volte nella sequenza.")

        print(f"Il numero {x} compare per la prima volta in {pos} nella sequenza.")

        print(f"La somma dei numeri diversi da x è {somma}.")

        