
# index operator gives acces to the sequence of element (str, list , tuples)

name = 'charles Bessong Tabot'

if(name[0].islower()):
  name = name.capitalize()
  
firstName = name[:7].upper()
print(firstName)
lastName = name[8:].lower()
print(lastName)
lastCharacter = name[-1]
print(lastCharacter)