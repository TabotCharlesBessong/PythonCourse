
from cmath import e


try:
  nume = int(input("Enter a number to divide: "))
  deno = int(input("Enter a number to devide by: "))
  res = nume / deno 

except ZeroDivisionError as e:
  print(e)
  print("You cant devide by zero")
except ValueError as e:
  print(e)
  print("Enter only numbers please")
  
except Exception as e:
  print(e)
  print("Something went wrong")  
else:
  print(res)
finally:
  print("This will always execute")