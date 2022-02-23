
import random

x = random.randint(1,6)
print(x)
y = random.random()
print(y)
y = random.random()

myList = ['rock','paper','scissors']
z= random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']

random.shuffle(cards)

print(cards) 