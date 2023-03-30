"""Create a class that captures students. Each student has a first name, last name, class year, and 
major. Create two examples of students"""
class Student:
    def __init__(self,fn,ln,year,major) -> None:
        self.fn=fn
        self.ln=ln
        self.year=year
        self.major=major
    def showStudent(self):
        print("First Name",self.fn)
        print("Last name",self.ln)
        print("Class Year",self.year)
        print("Major",self.major)

s1=Student('abc','xyz',1,'CSE')
s2=Student('pqr','wsd',2,'CSE')
s1.showStudent()
s2.showStudent()