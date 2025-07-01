# Default argument 
def show_employee(name:str, salary=9000):
    print(f"Nome: {name}, Salario: {salary}")
    print("Name:", name, "Salary", salary)

show_employee("Ben", 12000)
show_employee("Jessa")

