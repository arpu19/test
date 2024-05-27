class emp:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def my_reslutshow(self):
        print (self.name,":",self.age,":",self.salary)

e1=emp("kavita",17,17000) 
e1.my_reslutshow() 





class school:
    def __init__(self,name,age,std):
        self.name= name
        self.age=age
        self.std=std
    def my_info(self):
        print("name of student:",self.name,"\nage of student:",self.age,"\nstd: of student: ",self.std)

s1=school("arpita",19,"2 year")  


s1.my_info()   
        