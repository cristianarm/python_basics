
# First program
# import library
import math

#function
def factorial(n):
  '''Computes the factorial of an integer "n"'''
  if n < 0:
    raise ValueError('Number must be non-negative')

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


if __name__ == '__main__':

  # list
  fruits = ['orange', 'strawberry', 'apple']
  for i, fruit in enumerate(fruits):
    print(str(i) +","+ fruit)

  # call functions and use libraries 
  value2  = factorial(9)
  result2 = '\nThe sum of {a} and {b} is: {c}'.format(a=value2, b=math.pi, c=(value2 + math.pi))
  print(result2)

  #handling error
  try:
    factorial(-1)
  except ValueError as e:
    print("\n"+ str(e))