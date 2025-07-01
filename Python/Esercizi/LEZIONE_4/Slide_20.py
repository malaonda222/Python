def get_user(myname:str, myrole:str) -> dict[str, str]:
    return{"name": myname, "role": myrole}

user = get_user("Alice", "Admin")
print(user["name"])
print(user["role"])


def user(myname:str, myrole:str) -> dict[str, str]:
    return{"name": myname, "role": myrole}

ur = user("Lisa", "coordinator")
print(ur["name"])
print(ur["role"])

