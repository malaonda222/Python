# Funzione con più di un valore (tupla, lista, dizionario)

def get_coordinates() -> list[float]:
    return[12.5, 45.8]

coords = get_coordinates()
print(coords[0], coords[1], sep= ", ")

def get_numbers() -> list[float]:
    return[12, 10]

numbers = get_numbers()
print(numbers[0], numbers[1], sep= ", ")

def get_coordinates() -> list[float, int]:
    return[12.5 , 10]

coords = get_coordinates()
print(coords[0], coords[1], sep= ", ")