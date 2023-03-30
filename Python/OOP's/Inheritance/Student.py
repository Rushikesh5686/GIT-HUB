"""Write a program to implement a class “student” with the following members. Name of the 
student. Marks of the student obtained in three subjects. Function to assign initial values. 
Function to compute total average. Function to display the student’s name and the total marks. 
Write an appropriate main() function to demonstrate the functioning of the above"""

class Student:
    def __init__(self,n,m1,m2,m3) -> None:
        self.n=n
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def Avg(self):
        T=self.m1+self.m2+self.m3
        A=T/2
        print("Average",A)
    def show(self):
        print("Student name",self.n)
        T=self.m1+self.m2+self.m3
        print("Total marks",T)
        
s1=Student("abc",80,75,85)
s2=Student("xyz",70,82,86)
s1.show()
s1.Avg()
s2.show()
s2.Avg()