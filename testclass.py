class Student:
    def __init__(self,name,roll):
        self.name= name
        self.roll= roll

    def my_show(self):
        print(self.name,": ",self.roll)
    
  
        
obj1=Student("annu",1)
obj1.my_show()

class emp:
    def _init_(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def my_reslutshow(self):
        print(self.name,":"self.age,":"self.salary)

e1=emp("kavita",17,17000)  
e1.myresultshow()     