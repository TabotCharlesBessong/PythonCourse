

# thread = flow  of execution like seperate order list of instructions 
# GIL  global interpreter lock allows only one thread to hold the control of the python interpreter 

# cpu bound = program / task spends most of its time waiting for internal events using multiprocessing

# io bound = program/task spends waiting for external events using multiprocessing

import threading
import time

def eat():
  time.sleep(3)
  print('You eat breakfast')
def drink():
  time.sleep(4)
  print('You drink coffee')
def study():
  time.sleep(5)
  print('You study')
  
eat()
drink()
study()
# print(threading.active_count())
# print(threading.enumerate())