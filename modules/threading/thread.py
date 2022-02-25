

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

x =threading.Thread(target=eat,args=())
x.start()

y =threading.Thread(target=drink,args=())
y.start()


z =threading.Thread(target=study,args=())
z.start()

x.join()  
y.join()
z.join()

# eat()
# drink()
# study()
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())