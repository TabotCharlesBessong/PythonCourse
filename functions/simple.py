
# simple
# from turtle import title


def hello(fName,lName,age):
  print('Hello '+ fName+ " "+lName)
  print('You are '+ str(age)+' years old')
  print('Have a nice day')

hello('Charles','Bessong Tabot','19')

# return
def mul(n1,n2):
  return n1 * n2
x = mul(24,47)
print(x)

# keyword arguments
def key (f,m,l):
  print("Hello "+f+" "+m+" "+l)
key(f='Python',m='Javascript',l='c++')

def add(*stuffs):
  # args pack all argument into a single one 
  # args are tuple so unchangable so to change it , you need to make it a list 
  sum = 0
  stuffs = list(stuffs)
  # stuffs[0] = 0
  for i in stuffs:
    sum += i
  return sum
print(add(1,2,3,4,5,6))

# **kwargs paramenters will pack all argument into a dictionaries

def kwack(**a):
  print('Hello '+ a['first'] + " " + a['last'])
  print('hello',end=" ")
  for k,v in a.items():
    print(v,end=" ")

kwack(title="Mr .",first='Bro',middle="Dude",last="Code",other="Me")