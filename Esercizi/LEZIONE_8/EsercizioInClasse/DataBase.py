from Course import Course
from Faculty import Faculty

class Faculty:
    def __init__(self, name: str, id: str):
        self._name = name 
        self._id = id
        self._course = dict() 
    
    def get_name(self) -> str:
        return self._name 
    
    def get_id(self) -> str:
        return self._id 
    
    def add_courses(self, f: Faculty, c: Course):
        if f.get_id() not in self._courses:
            self._courses[f.get_id()] = dict()
        
        self._courses[f.get_id()][c.get_id()] = c 

    def print_course_info(self):
        for faculty_id, faculty_data in self._courses.items():
            for course_id, course in faculty_data.items():
                print(faculty_id, course.get_info())

            



    
    

    
