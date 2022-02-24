
# multilevel inheritance happens when a child class  inherits properties from another child class 

class Organims:
  alive = True
  
class Animal(Organims):
  
  def eat(self):
    print("This animal is eating")
    
class Dog(Animal):
  
  def bark(self):
    print("this dog is barking")
    
dog = Dog()
# print(dog.alive)
# print(dog.eat())
dog.bark()
dog.eat()



