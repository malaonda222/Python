def proDict() -> dict[tuple, int]:
    interi_x: list[int] = [x for x in range(0, 101)]
    interi_y: list[int] = [y for y in range(2, 89, 2)]
    
    d: dict[tuple, int] = {}
    for x in interi_x:
        for y in interi_y:
            d[x, y] = x*y
    return d


if __name__ == '__main__':
    d: proDict = proDict()
    chiavi = [(13, 88), (83, 56), (71, 44)]

    for k in chiavi:
        if k in d:
            print(f"Prodotto {k[0]} x {k[1]} = {d[k]}")
        else:
            print(f"Chiave {k} non presente nel dizionario.")
