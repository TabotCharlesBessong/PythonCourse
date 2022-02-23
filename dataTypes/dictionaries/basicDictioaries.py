
# dictionaries a changable , unordered and unique values collections 

capitals = {
  'USA':'washington DC',
  'India':'New Dehli',
  'China':'Beijing',
  'Russia':'Moscow'
}
print(capitals)

capitals.update({'Germany':'Berlin'})
print(capitals)
capitals.update({'USA':'Las Vegas'})
print(capitals)
capitals.pop('China')
print(capitals)
capitals.clear()
print(capitals)

for key,value in capitals.items():
  print("\n")
  print(key,value)