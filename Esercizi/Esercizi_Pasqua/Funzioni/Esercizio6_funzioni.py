def create_contact(nome: str, email: str=None, telefono: int=None) -> dict:
    dictionary = {
        "profile": nome,
        "email": email, 
        "telefono": telefono
        }
    return dictionary         

def update_contact(dictionary: dict, nome: str, email: str = None, telefono: int = None) -> dict:
    if email is not None: 
        dictionary["email"] = email
    if telefono is not None:
        dictionary["telefono"] = telefono
    return dictionary


contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))