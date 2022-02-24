
import os


source = 'test.txt'
destination = 'C:\\Users\\CHARLES\\Documents\\copy.txt'

try:
  if os.path.exists(destination):
    print('This file already exist')
  else:
    os.replace(source,destination)
    print(source+" was moved")
except FileNotFoundError:
  print(source+" was not found")