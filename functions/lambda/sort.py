


students = (
  ('w','F',60),
  ('b','B',72),
  ('c','A',33),
  ('m','D',36),
  ('d','C',78),
)

grade = lambda grades:grades[1]
percentage = lambda percentages:percentages[1]

sortedStudents = sorted(students,key=grade)
sortedStudents1 = sorted(students,key=percentage)

for i in sortedStudents:
  print(i)

print("---------------------------")
  
for k in sortedStudents1:
  print(k)