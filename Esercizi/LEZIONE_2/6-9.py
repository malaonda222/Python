favorite_places = {
    "Lisa":["Italia", "Kenya", "Giappone"],
    "Marco":["Svizzera", "Russia"],
    "Riccardo":"Colombia"
}

# for person in favorite_places:
#     print(f"nome: {key['nome']}, posti preferiti {key['posti']}\n")


for person, place in favorite_places.items():
    print(f"nome: {person}, posto preferito: {place}")