class Student:
    def __init__(self,name,age,weight,) :
        
        self.name=name
        self.age= age
        self.weight=weight
    
    def show(self):
         print("Name is student = ",self.name,"\nAge of student = ",self.age,"\nWeight of student = ",self.weight)


class Sport(Student):
    def __init__(self,name,age,weight,marks):
        super().__init__(name,age,weight)
        self.marks=marks
        

    def display(self):
        print("student Marks in sprots =",self.marks)


class Topper(Sport):
    def __init__(self, name, age, weight, marks,Totalmarks,Englishmarks,mathsmarks):
        super().__init__(name, age, weight, marks)
        self.Totalmarks=Totalmarks
        self.Englishmarks=Englishmarks
        self.mathsmarks=mathsmarks

    def result(self):
        print("english marks = ",self.Englishmarks,"\nmaths marks = ",self.mathsmarks,"\n Total marks of student =",self.Totalmarks)



t1=Topper("arpita",19,38,100,100,50,50)
t1.show()
t1.display()
t1.result()
             