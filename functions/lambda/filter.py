# filters create a seperate list of element that meets a certain condition 

friends = [
  ('Rachel',19),
  ('Monica',18),
  ('Phoenix',17),
  ('Joey',18),
  ('Chandler',16),
  ('Ross',20)
]

age = lambda data:data[1] >= 18
age1 = lambda dat:dat[1] == 18

drinkingMates = list(filter(age,friends))
yesterday = list(filter(age1,friends))

print(drinkingMates)
print("\n")
print(yesterday)