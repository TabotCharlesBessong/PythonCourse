


# from pip import main

from multiprocessing import cpu_count
from multiprocessing.dummy import Process
import time


def counter(num):
  count = 0
  while count < num:
    count += 1
    # print(count)
def main():
  print(cpu_count())
  a = Process(target=counter,args=(200000000,))
  b = Process(target=counter,args=(200000000,))
  c = Process(target=counter,args=(200000000,))
  d = Process(target=counter,args=(200000000,))
  
  a.start()
  b.start()
  c.start()
  d.start()
  
  a.join()
  b.join()
  c.join()
  d.join()
  
  print('Finished in: ',time.perf_counter()," milliseconds")

if __name__ == '__main__':
  main()