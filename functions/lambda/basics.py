
# a lambda functipn are written in one line , when they are needed for a short period of time . they use the lambda function 
# they can take multiple parameters but have only one expression
double = lambda x: x + 2
multiply = lambda x,y:x * y 
add = lambda x,y,z:x+y+z 
fullName = lambda firstName , lastName : firstName+" "+lastName
ageCheck = lambda age:True if age >= age else False
print(ageCheck(19))

print(multiply(8,9))
print(fullName('Charles','Bessong Tabot'))