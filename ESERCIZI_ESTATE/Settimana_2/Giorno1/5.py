'''Logica: Trova tutti i numeri perfetti tra 1 e 1000.'''

def perfetto(numero: int) -> bool:
    lista_divisori = []
    for i in range(1, numero):
        if numero % i == 0:
            lista_divisori.append(i)
    if numero == sum(lista_divisori):
        return True
    else:
        return False


def perfetti_1_1000():
    lista_numeri: list = []
    i = 1
    while i <= 1000:
        numero = i
        if perfetto(numero):
            lista_numeri.append(numero)
            i += 1
        else:
            i += 1
    return lista_numeri

print(perfetti_1_1000())