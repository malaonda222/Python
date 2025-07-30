'''Conta le occorrenze dei caratteri in una stringa.'''

def occorrenze(stringa1: str) -> dict[str, int]:
    frequenze = {}
    for element in stringa1:
        if element not in frequenze:
            frequenze[element] = 1
        else:
            frequenze[element] += 1
    return frequenze


stringa1: str = "binjgjcljdk"
print(occorrenze(stringa1))
