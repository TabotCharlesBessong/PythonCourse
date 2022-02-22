
temp  = int(input('what is the temp in your area?: '))

if temp >= 0 and temp <=30:
  print('Temp is good today')
  print('Go outside')
elif temp < 0 or temp > 30:
  print('Temp is bad today')
  print('Dont go outside')
else:
  print("We dont know")