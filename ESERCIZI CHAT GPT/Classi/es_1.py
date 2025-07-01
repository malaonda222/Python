class Student:
    total_students = 0
    
    def __init__(self, nome:str, età:int):
        self.nome = nome
        self.età = età
        Student.total_students += 1
    
    @classmethod
    def get_total_student(cls):
        return cls.total_students

student1 = Student("Lisa", 26)
student2 = Student("Riccardo", 33)
student3 = Student("Simone", 21)

print(f"Il totale degli studenti creati è: {Student.get_total_student()}")
