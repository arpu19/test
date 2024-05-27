class Employee:
    def __init__(self,fname,lname, salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

    def my_emp(self):
       
        print("\nfrist name of empyolee:",self.fname,"\nlast name of employee:",self.lname,"\nemployee salary amount:",self.salary)    


class  Emp_info(Employee):
    def __init__(self,fname,lname,salary,address,gender) :
        super().__init__(fname,lname,salary)
        self.address= address
        self.gender= gender

    
    def display(self):
        print("\nemployee gender :",self.gender,"\nemployee home address:",self.address)


class Job_info(Emp_info):
    
    def __init__(self,fname,lname,salary,address,gender,package,time,shift):
        super().__init__(fname,lname,salary,address,gender)
        self.package=package
        self.time=time
        self.shift=shift

    def result(self):
        print("\nemployee package as per year :",self.package,"\nworking time of employee :",self.time,"\nshift of worker : ",self.shift)



emp1=Job_info("arpita","yadav",59000,"tulshet pada","female",70000000, "five hours","Day")
emp1.my_emp()
emp1.display()
emp1.result()

        
        