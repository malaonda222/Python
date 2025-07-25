def create_contact(nome: str, email: str|None, telefono: str|None) -> dict[str, str|None, str|None]:
    new_dict = {}
    new_dict["profile"] = nome 
    new_dict["email"] = email
    new_dict["telefono"] = telefono

    return new_dict

print(create_contact("Lisa"))
print(create_contact(nome="Nico"))


def update_contact(dictionary: dict, email: str|None, telefono: str|None) -> dict[str, str|None, str|None]:
    if email is not None:
        dictionary["email"] = email 
    if telefono is not None:
        dictionary["telefono"] = telefono 
    return dictionary

contatto = create_contact("Lisa", "bandinelli@gmail.com", telefono=None)
print(create_contact("Lisa", "bandinelli@gmail.com", telefono=None))
print(update_contact(contatto, "bandinelli.lisa@gmail.com", telefono="36674895038"))

