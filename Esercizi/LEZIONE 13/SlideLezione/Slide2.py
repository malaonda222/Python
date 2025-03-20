def countdown(n:int) -> None:
    if n >= 0:
        while n >= 0:
            print(n)
            n = n - 1
    else:
        print("Errore, il numero inserito non deve essere negativo.")

countdown(-5)
countdown(5)

