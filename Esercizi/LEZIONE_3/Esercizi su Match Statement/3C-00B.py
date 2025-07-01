# chiedere all'utente di inserire nome e genere
nome = input("Inserisci il tuo nome: ")
genere = input("Inserisci genere. Digitare \"m\" per maschio e \"f\" per femmina: ")

# statement match
match (nome, genere):
    case (nome, "m"):
        print(f"Nome: {nome} \nGenere Maschio")
    case (nome, "f"):
        print(f"Nome: {nome} \nGenere Femmina")
    case _:
        print("Non è possibile generare un documento di identità")
              