
try:
  with open('token.txt') as file:
    print(file.read())
except FileNotFoundError:
  print("That file was not found")