def describe_pet(animal_type: str, pet_name: str) -> str:
    return f"Descrizione dell'animale: {animal_type} - {pet_name}"


print(describe_pet("gatto", "Nino"))
print(describe_pet(animal_type="zebra", pet_name="Poli"))