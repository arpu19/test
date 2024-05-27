class X:
    def __init__(self,A) :
        self.A=A
    
    def show(self):
        print("A is belong  class:",self.A)


class V:
    def __init__(self,A,B):
        self.B=B

    def display(self):
        print("B is belong to calss:",self.B)



class Z(X,V):
    def __init__(self, A, B, C):
        X.__init__(A)
        V.__init__(B)
        self.C=C

    def result(self):
        print(" is belong toh class:",self.C)
        


z1=Z("my","self","arpita")
z1.show()
z1.display()
z1.result()
