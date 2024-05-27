class A:
    def __init__(self,num) :
        self.num= num
        
    def show(self):
        print("id",self.num)


class B(A):
    def __init__(self, num,name):
        super().__init__(num)
        self.name=name

    def disply(self):
        print("name",self.name)

b1=B(1000,"arpita")
b1.show() 
b1.disply()
