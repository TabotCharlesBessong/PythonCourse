
# super function is used to get access to the  method of the parent  class 
# it stops you from repearing yourself

class Rectangle:
  
  def __init__(self,length,width):
      self.length = length
      self.width = width
      
class Square(Rectangle):
  
  def __init__(self, length, width):
      super().__init__(length, width)
      # self.length = length
      # self.width = width
      
  def area(self):
    return self.length * self.width
  
class Cube(Rectangle):
  def __init__(self, length, width,height):
      super().__init__(length, width)
      # self.length = length
      # self.width = width
      self.height = height
  def volume(self):
    return self.length * self.width * self.height
      
square = Square(4,7)
cube = Cube(4,7,23)

print(square.area())
print(cube.volume())