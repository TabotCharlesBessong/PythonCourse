
utensils = {'fork','spoon','knife','plate'}
dishes = {'bowl','plate','cup','knife'}

print(utensils)
print(dishes)

utensils.add('napkin')
print(utensils)
utensils.remove('fork')
print(utensils)
utensils.clear()
print(utensils)
dishes.update(utensils)
print(dishes)
dinningTable = dishes.union(utensils)
print(dinningTable)
print(utensils.intersection(dishes))
print(utensils.issubset(dishes))
print(dishes.issuperset(utensils))
print(utensils.issuperset(dishes))
print(utensils.difference(dishes))
meal = dishes.copy()
print(meal)

for x in dinningTable:
  print(x)