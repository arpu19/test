class student():
    def __init__(self, id ,name):
        self.id=id
        self.name=name
    def mystudent(self):
        print("student id",self.id,"student name:",self.name)


class Details(student):
    def __init__(self, id ,name,year):
       super().__init__(id,name)
       self.collegeyear=year
    def myself(self):
        print("id of sutdent:",self.id,"Name of student:",self.name,"passed of year",self.collegeyear)


s1=Details(100,"arpita",2025)
s1.myself()
