
from calendar import c
import time

for i in range(10):
  print(i + 1)
  print("\n")
for j in "Charles Bessong":
  print(j)
  
for k in range(0,20,2):
  print(k * k)
  print("\n")
  
for sec in range(10,0,-1):
  print(sec)
  time.sleep(1)
print("Ein gut Neu jahr")

rows = int(input('How many rows do you want?: '))
columns = int(input('How many columns do you want?: '))
symbol = input("Whats shape do you want to use")

for l in range(rows):
  for m in range(columns):
    print(symbol , end="")
  print()