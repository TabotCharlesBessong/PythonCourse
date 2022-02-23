
number = 1000
animal = "cow"
item = "moon"

print("This number is {:.3f}".format(number))
print("This number is {:,}".format(number))
print("This number is {:b}".format(number))
print("This number is {:o}".format(number))
print("This number is {:X}".format(number))
print("This number is {:E}".format(number))

print("The "+animal+" jumped over the "+ item)
print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {1}".format(animal,item))
# print("The {} jumped over the {}".format(animal="cow",item="moon"))
# the above is a  key word argument 

text = "The {} jumped over the {}"
print(text.format(animal,item))

name = "Charles"
print("Hello , my name is {:20}. Nice to meet you".format(name))
print("Hello , my name is {:>20}. Nice to meet you".format(name))
print("Hello , my name is {:^20}. Nice to meet you".format(name))
