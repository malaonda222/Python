#People

my_dict = {
    "first_name":"Giuseppe",
    "last_name":"Ungaretti",
    "age":88,
    "city":"Torino"
}

my_dict_2 = {
    "first_name":"Lisa",
    "last_name":"Bandinelli",
    "age":26,
    "city":"Firenze"
}

my_dict_3 = {
    "first_name":"Nico",
    "last_name":"Valenzuela",
    "age":36,
    "city":"Santiago"
}
list_people = [my_dict, my_dict_2, my_dict_3]
print(list_people)

for key in list_people:
    print(f"nome: {key['first_name']}\ncognome: {key['last_name']}\netà: {key['age']}\ncittà: {key['city']}\n")


