class Student:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id= id

    def show(self):
        print("name of student:",self.name,"\nage of stuent:",self.age,"\nId of student:",self.id)

class Sports(Student):
    def __init__(self,name,age,id,marks):
          super().__init__(name,age,id)
          self.marks=marks

    def display(self):
        print("marks in sports",self.marks)


s1=Sports("arpita",19,1234,100)
s1.show()
s1.display()

              
              
    
    