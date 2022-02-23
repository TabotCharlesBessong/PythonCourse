




food = ['pizza','hamburger','hotdog','spagetti','pudding']
# this is a list and it is just like an array in js

food[0] = 'eru'
# here , we are simply replacing whats at index 0 with eru

for x in food:
  print(x)

food.append('iceCream')
# we are adding ice cream to our list and by defaul it goes to the last index
print(food)
food.remove('hotdog')
# we remove hotdog from our list
print(food)
food.pop()
# we remove the last element from our list
print(food)
food.insert(1,'cake')
# we insert cake at index 1 so the rest will readjust by index += 1
print(food)
food.sort()
# here we sort our  list in order
print(food)
food.clear()
# we delete every element of our list 
print(food)