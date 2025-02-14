cities = {
    "Parigi":{
        "Paese":"Francia",
        "Popolazione":"3 milioni",
        "Fact":"Viene chiamata la città dell'amore",
        "Celebrity":"Omar Sy",
        "Language":"Francese"
    },

    "Rome":{
        "Paese":"Italia",
        "Popolazione":"4 milioni",
        "Fact":"Tutte le strade portano a Roma",
        "Celebrity":"Francesco Totti",
        "Language":"Italiano"

    },

    "Amsterdam":{
        "Paese":"Olanda",
        "Popolazione":"1 milione",
        "Fact":"La Venezia del Nord",
        "Celebrity":"Van Gogh",
        "Language":"Olandese"
    },

    "Barcellona":{
        "Paese":"Spagna",
        "Popolazione":"2 milioni",
        "Fact":"La città della movida",
        "Celebrity":"Picasso",
        "Language":"Spagnolo"
    }

}

for city, info in cities.items():
    # print(f"La città di {city} ha le seguenti caratteristiche: {info}\n")
    print(f"La città in questione è {city};")
    print(f"{city} si trova in {info['Paese']};")
    print(f"La popolazione ammonta a {info['Popolazione']};")
    print(f"Fun Fact: {info['Fact']};")
    print(f"Una celebrità di questo Paese è {info['Celebrity']};")
    print(f"La lingua ufficile è: {info['Language']}\n")