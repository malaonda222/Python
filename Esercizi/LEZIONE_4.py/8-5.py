# Cities
def describe_city(city:str, country="Italy"):
    return f"{city} is in {country}"

print(city="Florence")
print(city="Bologna")
print(city="Ginevra", country="Svizzera")



def describe_city(name: str, country="Spain"):
    return f"{name} is in {country}"

print(describe_city("Seville"))
print(describe_city(name="Madrid"))
print(describe_city(country="Colombia", name="Medellin"))
