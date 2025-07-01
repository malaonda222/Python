'''### Classe Course:
La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) 
e una lista di gruppi (groups).
- Metodi:
    - register(student): Registra uno studente nel primo gruppo disponibile 
    che non ha ancora raggiunto il limite di studenti.
    - get_groups(): Restituisce la lista dei gruppi nel corso.
    - add_group(group): Aggiunge un gruppo al corso.'''

class Course:
    def __init__(self, name:str):
        self.name = name
        self.groups = []
        
    def register(self, student:str):
        for group in self.groups:
            if len(group.get_students()) < group.get_limit():
                group.add_student(student)
                return
        print(f"Nessun gruppo disponibile con posti liberi per lo studente {student}.")
    
    def get_groups(self) -> list[str]:
        return self.groups
    
    def add_group(self, group:str):
        self.groups.append(group)