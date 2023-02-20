
print('Welcome to our millage converter calculator')

n1 = 1
d1 = 1.64

def mile_converter(num,operation):
  operation = int(input('Enter 1 for kilometers to miles conversion\nEnter 0 for miles to kilometers conversion:\n'))
  
  if operation == 0:
    # d2 = 0
    n2 = int(input("How many miles do you want to convert to kilometers: "))
    d2 = round((d1*n2)/n1,2)
    print(f"{n2} miles gives {d2} kilometers")
    return
  elif operation == 1:
    d2 = int(input("How many kilometers do you want to convert to miles: "))
    n2 = round((n1 * d2) / d1, 2)
    print(f"{d2} kilometers gives {n2} miles")
    return
  else:
    print('Please enter the correct choice')
    mile_converter(num=1,operation='')  
  
  

mile_converter(num=1,operation='')