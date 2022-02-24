 
# from typing_extensions import Self
from car import Car

# print(Car.drive())
# Car.drive()

car1  = Car("Tesla","Model3",2022,"Green")
car1.wheels = 2  #class variables 

print(car1.make)  #instance variables
print(car1.model)  #instance variables
print(car1.color)  #instance variables
print(car1.year)  #instance variables

car1.drive()
car1.stop()