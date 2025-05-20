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


# soluzione Profe
def blackjack_hand_total(cards:list[int]) -> int:
    total:int = sum(cards)  # Calcola la somma iniziale dei valori delle carte
    num_aces:int = cards.count(11)  # Conta quanti assi (valore 11) sono presenti nella mano
    
    # Se il totale supera 21 e ci sono assi, riduci il valore degli assi a 1
    while total > 21 and num_aces > 0:
        total -= 10  # Cambia un asso da 11 a 1 per ridurre il totale
        num_aces -= 1  # Aggiorna il conteggio degli assi modificati
    
    return total  # Restituisce il valore totale della mano