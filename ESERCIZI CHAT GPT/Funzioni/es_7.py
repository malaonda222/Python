def somma_lista_numeri(lista):
    return sum(lista)

def main():
    input_numeri = input("Inserisci una lista di numeri separati da uno spazio: ")
    lista_numeri = [int(num) for num in input_numeri.split()]
    somma = somma_lista_numeri(lista_numeri)

    print(f"La somma dei numeri nella lista è: {somma}.")


main()


