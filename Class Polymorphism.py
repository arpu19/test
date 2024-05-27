class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Brand: ",self.brand)
    print("model: ",self.model)

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")
    

class Plane:
  def __init__(self,brand,model) :
    self.brand = brand
    self.model = model
  def move(self):
    print("FLY")

Car1= Car ("thar","Mustang")
Boat1= Boat("airpods","Touring 20")
Plane1 = Plane("Boeing", "747")
Car1.move()

   
    
