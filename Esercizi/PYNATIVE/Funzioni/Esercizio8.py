# Numeri pari compresi tra 4 e 30
def numeri_pari():
    lista_pari = []
    for item in range(4, 30, 2):
        lista_pari.append(item)
    print(lista_pari)

numeri_pari()