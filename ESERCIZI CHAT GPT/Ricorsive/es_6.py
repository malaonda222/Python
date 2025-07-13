def recursive_potenza(a: int, b: int) -> int:
    if b == 0:
        return 1
    if b == 0 and a == 0:
        raise ValueError("Indefinita")
    return a * recursive_potenza(a, b-1)

print(recursive_potenza(2, 5))