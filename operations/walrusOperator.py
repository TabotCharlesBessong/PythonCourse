

# happy = True
# print(happy)

print(happy := True)

foods = list()


# while True:
  # food = input("what food do you like?: ")
  # if food =='quit':
    # break
  # foods.append(food)
  
while food := input("what food do you like?: ") != 'quit':
  foods.append(food)
  
print(foods)