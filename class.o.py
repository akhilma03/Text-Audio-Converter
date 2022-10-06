class Student:
    def __init__(self,a1,a2):
        self.a1=a1
        self.a2=a2

    def __add__(self,other):
        a1 = self.a1+other.a1
        a2 = self.a2+other.a2

        c = Student(a1,a2)
        return c


ad = Student(10,30)
ad1 = Student(30,50)  
s=ad+ad1          

print(s.a1)
