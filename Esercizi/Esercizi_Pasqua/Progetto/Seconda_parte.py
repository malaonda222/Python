'''### Classi Person, Student e Lecturer:
La classe Person rappresenta una persona con un codice fiscale (cf), un nome (name),
 un cognome (surname), un'età (age).
Le classi Student e Lecturer ereditano da Person.
Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha 
il seguente metodo:
    - set_group(group): Associa un gruppo di studio allo studente

### Classe Group:
La classe Group rappresenta un gruppo di studio. Ogni gruppo ha un nome (name), 
un limite di studenti (limit), una lista di studenti (students) e una lista di docenti (lecturers).
- Metodi:
    - get_name(): Restituisce il nome del gruppo
    - get_limit(): Restituisce il limite di studenti nel gruppo
    - get_students(): Resituisce la lista di studenti nel gruppo
    - get_limit_lecturers(): Restituisce il limite di docenti nel gruppo. E' consentito 1 docente 
    ogni 10 studenti. Il gruppo può avere almeno 1 docente, anche se ci sono meno di 10 studenti.
    - add_student(student): Aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato raggiunto.
    - add_lecturer(lecturer): Aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto.'''

class Person:
    def __init__(self, cf:str, name:str, surname:str, age:int):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age
    
    def __str__(self):
        return f"{self.name} {self.surname}, cf: {self.cf}, age: {self.age}."
        
class Student(Person):
    def __init__(self, cf:str, name:str, surname:str, age:int):
        super().__init__(cf, name, surname, age)
        self.group = None
    
    def set_group(self, group:str) -> None:
        self.group = group
    
    def __str__(self):
        return f"Student: {super().__str__()}."
        
class Lecturer(Person):
    def __init__(self, cf:str, name:str, surname:str, age:int):
        super().__init__(cf, name, surname, age)
        
    def __str__(self):
        return f"Lecturer: {super().__str__()}."

class Group:
    def __init__(self, name:str, limit:int):
        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []
        
    def get_name(self) -> str:
        return self.name
    
    def get_limit(self) -> int:
        return self.limit 
    
    def get_students(self) -> list[int]:
        return self.students
    
    def get_limit_lecturers(self):
        return max(1, (len(self.students) + 9) // 10)
    
    def add_student(self, student):
        if len(self.students) < self.limit:
            self.students.append(student)
            student.set_group(self)

    def add_lecturer(self, lecturer):
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)