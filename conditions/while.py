
# from tkinter.font import names

# from time import time
# from calendar import c

# with break , if a condition is met , we stop the execution of the loop 
# with the continue statement , we continue if a condition is met  and that particulaer iteration is not executed so we move to the next 
# so whenever you want to escape , you use continue.
# to stop completely , you use break 

# pass control statement does nothing but act as a placeholder

count = 0
while 1 == 1 :
  count +=1
  if count == 50:
    break
  print('I am stuck in here')
  print("\n")
  # time.sleep(1)
  
  
name = ''
while len(name) == 0:
  name = input('Hey dude , whats your name?: ')
print("Hello "  + name)

while True:
  names = input('Enter your name: ')
  if names != '':
    break
print(names + "\n" )

tel = '123-4567-890'
for i in tel:
  if i == '-':
    continue
  print(i , end='')
print("\n")
  
print("Hey buddy")

for l in range (1,21):
  if i == 11:
    pass
  else:
    print(l)
