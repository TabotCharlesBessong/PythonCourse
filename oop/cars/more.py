

from turtle import color


class Car:
  color = None

class MotoCycle:
  color = None
  
bike1 = MotoCycle()
  
def changeColor(car,color):
  car.color = color
  
car1 = Car()
car2 = Car()
car3 = Car()

changeColor(bike1,"Orange")

changeColor(car1,"Green")
changeColor(car2,"Red")
changeColor(car3,"yello")

print(car1.color)
print(car2.color)
print(car3.color) 
print(bike1.color) 