def prodotto(a: int, b: int):
    if a == 0 or b == 0:
        return 0
    else:
        return a + prodotto(a, b-1)

print(prodotto(2, 3))
