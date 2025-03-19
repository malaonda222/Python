def alpha():
    print("Executing alpha")

def beta():
    alpha()
    print("Executing beta")

def gamma():
    print("Executing gamma")
    beta()

gamma()

'''Output:
Executing gamma
Executing alpha
Executing beta

Ordine di esecuzione: gamma() -> beta() -> alpha()

Ordine Rimozione: alpha() -> beta() -> gamma()
'''