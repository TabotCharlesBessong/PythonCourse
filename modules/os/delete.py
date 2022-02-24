

import os
import shutil


path = 'test.txt'
destination = 'C:\\Users\\CHARLES\\Documents\\copy.txt'
folder = 'output'

try:
  # os.remove(path)
  os.remove(folder)
  os.remove(destination)
  # os.rmdir(path)
  os.rmdir(folder)
  # shutil.rmtree(path)
  os.rmdir(destination)
  shutil.rmtree(destination)
except FileNotFoundError:
  print("File was not found")
except PermissionError:
  print("You do not have permission to to delete this!!!! ")
except OSError:
  print("The folder contains files")
else:
  print("Hello world")