#Pets
dict_1 = {
    "kind":"dog",
    "owner":"Jack"
}

dict_2 = {
    "kind":"cat",
    "owner":"Giusy"
}

dict_3 = {
    "kind":"squirrel",
    "owner":"Davide"
}

list_pets = [dict_1, dict_2, dict_3]
print(list_pets)

for pet in list_pets:
    print(f"animale: {pet['kind']}, proprietario: {pet['owner']}")