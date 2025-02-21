cities = {
    "Parigi":{
        "Paese":"Francia",
        "Popolazione":"3 milioni",
        "Fact":"Conosciuta come la città dell'amore"
    },

    "Rome":{
        "Paese":"Italia",
        "Popolazione":"4 milioni",
        "Fact":"Tutte le strade portano a Roma"
    },

    "Amsterdam":{
        "Paese":"Paesi Bassi",
        "Popolazione":"1 milione",
        "Fact":"La Venezia del Nord"
    }
}
print(cities)

for city, info in cities.items():
    # print(f"La città di {city} ha le seguenti caratteristiche: {info}\n")
    print(f"Citta: {city}")
    print(f"Paese: {info['Paese']}")
    print(f"Popolazione: {info['Popolazione']}")
    print(f"Fact: {info['Fact']}\n")