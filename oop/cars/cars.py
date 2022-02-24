 
# from typing_extensions import Self
from car import Car

# print(Car.drive())
# Car.drive()

car1  = Car("Tesla","Model3",2022,"Green")
print(car1.make)
print(car1.model)
print(car1.color)
print(car1.year)

car1.drive()
car1.stop()