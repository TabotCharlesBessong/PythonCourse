
# duck typing is a concept where an object is less important than the method of the class 
# if it walks like a duck , it qwuacks like a duck , then its a duck


class Duck:
  
  def walk(self):
    print('This duck is walking')
  def talk(self):
    print('This duck is qwuacking')
    
class Chicken:
  
  def walk(self):
    print('This chicken is walking')
  def talk(self):
    print('This chicken is clucking')
  def balk(self):
    print('This chicken is blucking')
    
class Person:
  def catch(self,duck):
    duck.walk()
    duck.talk()
    # duck.balk()
    print('You cought the critter')
    
duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
print("---------------")
person.catch(chicken)