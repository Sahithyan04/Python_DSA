class student :
    def __init__(self , name  , age , dept):
        self.name = name
        self.age = age
        self.dept = dept
    def all(self):
        return self.name , self.age , self.dept


class dept:
    def __init__(self, name , hod , s1 , s2):
        self.name  = name
        self.hod = hod
        self.s1 = s1
        self.students = [s1.all() , s2]
    def all(self):
        return self.name , self.hod , self.students

s1 = student("Ram" ,34 , "AIDS")
s2 = student("Suresh" , 99 , "AIDS")
AI = dept("AIDS ", "Doss ", s1,None)
print(AI.all())
