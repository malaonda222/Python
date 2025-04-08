import random 

def percorso(posizione_tart, posizione_lepre):
    percorso = ['_'] * 70 #lista vuota con 70 posizioni
    
    if posizione_tart == posizione_lepre:
        percorso[min(posizione_tart, 69)] = "OUCH!"

    else:
        percorso[min(posizione_tart - 1, 69)] = "T" #posizione della tartaruga
        percorso[min(posizione_lepre - 1, 69)] = "H" #posizione della lepre
    
    print(" ".join(percorso)) #lista delle posizioni le unisco in una singola stringa, separandole da uno spazio


def mosse_tartaruga(posizione_tart:list):
    movimento = random.randint(1, 10)
        
    if 1 <= movimento <= 5:
        print("Passo veloce!")
        posizione_tart += 3
    elif 6 <= movimento <= 7:
        print("Scivolata!")
        posizione_tart -= 6
    else:
        print("Passo lento.")
        posizione_tart += 1

    if posizione_tart < 1:
        posizione_tart = 1

    return posizione_tart


def mosse_hare(posizione_lepre:int):
    movimento = random.randint(1, 10)

    if movimento == 1 or movimento == 2:
        print("Riposo!")
    elif movimento == 3 or movimento == 4:
        print("Grande balzo!")
        posizione_lepre += 9
    elif movimento == 5:
        print("Grande scivolata!")
        posizione_lepre -= 12
    elif 6 <= movimento <= 8:
        print("Piccolo balzo!")
        posizione_lepre += 1
    else:
        print("Piccola scivolata")
        posizione_lepre -= 2

    if posizione_lepre < 1:
        posizione_lepre = 1
    
    return posizione_lepre


def gara():
    posizione_tart = 1
    posizione_lepre = 1
    print("BANG !!! AND THEY'RE OFF !!!")

    while posizione_tart < 70 and posizione_lepre < 70:
        posizione_tart = mosse_tartaruga(posizione_tart)
        posizione_lepre = mosse_hare(posizione_lepre)
    
        percorso(posizione_tart, posizione_lepre)

        if posizione_tart >= 70 and posizione_lepre >= 70:
            print("IT'S A TIE.")
            break 
        
        if posizione_tart >= 70:
            print("TORTOISE WINS! || VAY!!!")
            break 

        if posizione_lepre >= 70:
            print("HARE WINS || YUCH!!!")
            break 
    
gara()