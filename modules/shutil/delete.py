


import os
import shutil


path = 'test.txt'
destination = 'C:\\Users\\CHARLES\\Documents\\copy.txt'

try:
  os.remove(path)
  os.rmdir(path)
  shutil.rmtree(path)
except FileNotFoundError:
  print("File was not found")
except PermissionError:
  print("You do not have permission to to delete this!!!! ")
except OSError:
  print("The folder contains files")
else:
  print("Hello world")
