# chiamata per posizione

def describe_person(name:str, age:int, city:str):
    print(f"{name} is {age} and lives in {city}")

describe_person("Alice", 25, "Rome")

def greet(name:str, age:int) -> None:
    print("Hi my name is " + name + " and I'm " + str(age) + " years old.")

greet("Angela", 13)