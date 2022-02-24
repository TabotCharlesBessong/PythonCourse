
# zip in python aggregate element for 2 or more iterable , 
# they are stored in a tuple , list and dictionaries
# but stored in a tuple by default

userName = ['Dude','Bro','Mister']
passwords = ['pas#@wor%','abcx673','gurste871xs']

users = dict(zip(userName,passwords))
users2 = list(zip(userName,passwords))
users3 = tuple(zip(userName,passwords))
users4 = zip(userName,passwords)

print(type(users))

for key,value in users.items():
  print(key+" : "+ value)
  
for i in users2:
  print(i)
  
for l in users3:
  print(l)
  
for k in users4:
  print(k)