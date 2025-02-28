# Code rewiew

# Checking Usernames from 5-10.py

# definisci la lista originale degli user_names
current_users = [
    "Marco", "Lucia", "Sabina",
    "Filippo", "Riccardo"
]

# definisci una lista con nuovi user_names
new_users = [
    "Lucia", "Riccardo", "Giuseppe",
    "Lapo", "Edoardo"
]
# crea una nuova lista e imposta un ciclo per trasformare tutti i current_user in carattere minuscolo
new_current_users = [user.lower() for user in current_users]

# imposta ciclo per verificare se l'user è presente nella lista 
for user in new_users:
    if user in new_current_users:
        print(f"{user}, please insert a new username")
    else:
        print(f"The username {user} is available")


# Ordinal Numbers from 5-10.py

# creazione della lista con numeri da 1 a 9 e stampa dei suffissi ordinali 
numbers_list = [] # variabile più descrittiva rispetto a "lista"
for number in range(1, 10):
    numbers_list.append(number)
    # inserire uno spazio per migliorare la leggibilità e separare le sezioni del codice
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

# Extensions from 6-12.py

# imposta dizionari per le città e aggiungi informazioni

# scrivi le chiavi all'interno dei dizionari in minuscolo
cities = {
    "Parigi":{
        "paese": "Francia",
        "popolazione": "3 milioni",
        "fact": "Viene chiamata la città dell'amore",
        "celebrity": "Omar Sy",
        "language": "Francese"
    },

    "Rome":{
        "paese": "Italia",
        "popolazione": "4 milioni",
        "fact": "Tutte le strade portano a Roma",
        "celebrity": "Francesco Totti",
        "language": "Italiano"

    },

    "Amsterdam":{
        "paese": "Olanda",
        "popolazione": "1 milione",
        "fact": "La Venezia del Nord",
        "celebrity": "Van Gogh",
        "language": "Olandese"
    },

    "Barcellona":{
        "paese": "Spagna",
        "popolazione": "2 milioni",
        "fact": "La città della movida",
        "celebrity": "Picasso",
        "language": "Spagnolo"
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