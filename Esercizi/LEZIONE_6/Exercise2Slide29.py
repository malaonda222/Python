class Student:
    def __init__(self, name:str, studyProgram:str, age:int, gender:str):
        self.name = name
        self.studyProgram = studyProgram 
        self.age = age
        self.gender = gender
    
    def printInfo(self):
        print(f"Name: {self.name}, Indirizzo di studi: {self.studyProgram}, Età: {self.age}, Genere: {self.gender}\n")


io = Student("Lisa", "Data Analyst", 26, "femmina")
io.printInfo()

Nico = Student("Nico", "Python", 36, "maschio")
Nico.printInfo()

Giuseppe = Student("Giuseppe", "Cyber Security", 45, "maschio")
Giuseppe.printInfo()



class Person:
    personCount = 0
    def __init__(self, name:str):
        self.name = name
        self.personCount += 1

alice = Person("Alice W.")
bob = Person("Bob M.")
print(Person.personCount)



class Student:
    studentGrades = []
    def __init__(self, studentName:str, grade:int):
        self.name = studentName
        self.studentGrades.append(grade)
    
    def getGroupAverage(cls):
        avg = sum(cls.studentGrades) / len(cls.studentGrades)
        return avg