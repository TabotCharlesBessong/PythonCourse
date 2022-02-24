
# list comprehension = a way to create  a new list with less syntax can mimic certain lambda 

students = [100,90,80,70,60,45,74,63,0]

passedStudents = list(filter(lambda x: x >= 60 , students ))
passedStudents1 = [i for i in students if i >= 60]

passedStudents2 = [ i if i >= 60 else 'FAILED' for i in students]

print(passedStudents)
print(passedStudents1)
print(passedStudents2)

# with the list comprehension , you can write the program below in just 2 lines
squares = []
for i in range(1,11):
  squares.append(i * i)
print(squares)