
# map functions , applies functions to each item in an iterable (list , tuple , etc)

store = [
  ('shirt',22.00),
  ('pants',25.00),
  ('jacket',22.50),
  ('socks',10.00),
]

toEuros = lambda data: (data[0],data[1]*0.82)

storeEuro = list(map(toEuros,store))

for i in storeEuro:
  print(i)