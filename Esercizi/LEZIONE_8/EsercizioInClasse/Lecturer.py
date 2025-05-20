from Esercizi.LEZIONE_8.EsercizioInClasse.Person import Person 
from Course import Course 

class Lecturer(Person):
    def __init__(self, name, surname, cf, lista=...):
        super().__init__(name, surname, cf, lista)
        self.courses: list[Course]

    def add_course(self, c: Course):
        try:
            self._courses.append(c)
        except:
            self._courses: list[Course] = [c]
        
    def get_courses_info(self) -> None:
        for c in self._courses:
            course_name, course_id, course_mode = c.get.info()
            print(f"Course name = {course_name}, Course ID = {course_id}, Course mode = {course_mode}.")