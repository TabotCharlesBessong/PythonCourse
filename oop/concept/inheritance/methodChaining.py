

# method chaining = calling a multiple method sequentially 

class Car:
  def turnOn(self):
    print("You start the engine")
    return self
  
  def drive(self):
    print('You drive the car')
    return self
  
  def brake(self):
    print('You just pressed on the break')
    return self
  
  def turnOff(self):
    print('You just stoped the engine')
    return self
  
  
car = Car()

car.turnOn().drive()
car.brake().turnOff()

car.turnOn().drive().brake().turnOff()