
# deamon thread = a  thread that runs in the background not important for program to run .
# Your program wil not wait for a deamon thread to execute before executing 
# non-deamon threads stay alive until the program terminate
# They can be useful in garbage collection background execution , waiting for user input , long running processes 

import threading
import time


def timer():
  print()
  print()
  count = 0
  while True:
    time.sleep(1)
    count +=1
    print("Logged in for: ",count," seconds")
    
# with this code the thread will not stop its execution 
# to avoid this , you use deamon thread we give the attribute deamon = True
x = threading.Thread(target=timer,daemon=True)
x.start()
# this can also change from non-deamon to demon
# x.setDaemon(True)
print(x.isDaemon())
answer = input('Whats your answer: ')