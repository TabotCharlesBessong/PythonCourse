
# prevent user from creating an object of that class 
# compels user to override abstract method 
# They have  declaration but no implementation

from abc import ABC,  abstractmethod


class vehicle(ABC):
  
  @abstractmethod
  def go(self):
    pass
  
  @abstractmethod
  def stop(self):
    pass
  
class Car(vehicle):
  def stop(self):
    print('This car has stoped')
    
car = Car()
car.stop()

 