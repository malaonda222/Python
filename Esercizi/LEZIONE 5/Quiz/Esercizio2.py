# bust > 21
# se somma della mano supera 21 e c'è almeno un asso valutato 11 -> asso deve valere 1

def blackjack_hand_total(cards: list[int]) -> int:
    somma_carte = 0
    assi = 0

    
    for item in cards:
        if item == 1:
            assi += 1
        somma_carte += item
    
    while somma_carte > 21 and assi > 0:
        somma_carte -= 10
        assi -= 1

    return somma_carte

print(blackjack_hand_total([10, 1]))
   
