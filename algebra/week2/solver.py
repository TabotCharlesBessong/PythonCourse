from sympy import symbols
from sympy.solvers import solve
from sympy import factor

x = symbols('x')

eq = (x**2) + 6*x + 5
print("x = ",solve(eq,x))

y = symbols('y')

equ = input('Enter equation: 0 = ')

solution = solve(equ,y)
for s in solution:
  print('y = ',s)
  
equa = x**3 - 2*x**2 - 5*x + 6 
print(factor(equa))