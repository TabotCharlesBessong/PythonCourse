
# multiple inheritance , this is when a base class is derived from more than 1 parent class 

class Prey:
  
  def flee(self):
    print('This animal has to run all the time predators')

class Predator:
  
  def hunt(self):
    print('This animal hunst predators all the time')
    
class Rabbit(Prey):
  pass

class Hawk(Predator):
  pass

class Fish(Predator,Prey):
  pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.flee()
fish.hunt()

rabbit.flee()
hawk.hunt()