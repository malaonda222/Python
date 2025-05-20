from Lecturer import Lecturer 
from Student import Student 

class Group:
    def __init__(self, name: str, n_studenti: int):
        self._name = name 
        self._n_students = n_studenti 
        self.students = list()
        self.lecturers = list() 
    
    def get_name(self) -> str:
        return self._name 
    
    def get_limit(self) -> int:
        return self._n_students
    
    def get_students(self) -> list[Student]:
        return self._students 
    
    def get_limit_lecturer(self) -> int:
        if len(self._students) == 0:
            return 0
        elif len(self._students) < 10:
            return 1 
        else: 
            return len(self._students) // 10 
    
    def add_student(self, s: Student):
        if len(self._students) < self.get_limit():
            self._students.append(s)
    
    def add_student(self, l: Lecturer):
        if len(self.lecturer) < self.get_limit_lecturer():
            self._lecturers.append(l)

    
