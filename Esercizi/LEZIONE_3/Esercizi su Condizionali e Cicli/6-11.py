cities = {
    "Parigi":{
        "paese":"Francia",
        "popolazione":"3 milioni",
        "fact":"Conosciuta come la città dell'amore"
    },

    "Rome":{
        "paese":"Italia",
        "popolazione":"4 milioni",
        "fact":"Tutte le strade portano a Roma"
    },

    "Amsterdam":{
        "paese":"Paesi Bassi",
        "popolazione":"1 milione",
        "fact":"La Venezia del Nord"
    }
}
print(cities)

for city, info in cities.items():
    # print(f"La città di {city} ha le seguenti caratteristiche: {info}\n")
    print(f"citta: {city}")
    print(f"paese: {info['paese']}")
    print(f"popolazione: {info['popolazione']}")
    print(f"fact: {info['fact']}\n")