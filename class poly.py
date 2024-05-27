class car:
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand
    def show(self):
        print("color:",self.color)
        print("brand:",self.brand) 

class features:
    def __init__(self,price,engine):
        self.price=price
        self.engine=engine
    def see(self):
        print("price:",self.price)
        print("engine:",self.engine)

class parts():
    def __init__(self,Door,mirror):
         self.Door=Door
         self.mirror=mirror
    def show(self):
        print("Door:",self.Door)
        print("mirror",self.mirror)

        
    

car1=car("black","thar")   
car1.show()
features1=features("1500000","hot")
features1.see()
parts1=parts("side Door","side morror")
parts1.show()

        