
from cgitb import text


def loud(text):
  return text.upper()

def quiet(text):
  return text.lower()

def hello(func):
  text = func('ich liebe dich')
  print(text)
  
hello(loud)
hello(quiet)