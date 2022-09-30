print('\nassigning values to variables')
a = 'hello'
b, c = 10, 5.5
print('the value of a: ', a)
print('the value of b: ', b)
print('the value of c: ', c)

print('\nassignment of values in multiple lines')
sum = 1 + 2 + 3 + \
      4 + 5 + 6 + \
      7 + 8 - 9 

sum2 = (1 + 2 + 3 + 
    4 + 5 + 6 + 
    7 + 9 * 9)
    
print('the value of sum :',sum)
print('the value of sum2:',sum2)

import random
r= random.randint(sum, sum2)
if r >= 100:
    print('hit!')
    s = 5

if r >= 100: print('hit!'); s = 5

fruits = ['orange',
        'banana',
        'apple']

fruits = ['orange', 'banana', 'apple']

for x in fruits:
  if x == 'banana':
    continue
  print(x) 

print('\nComments') 
# Single comment
stars = ['sun', 'betelgeuse']

# Multi-line comment
# Multi-line comment
stars = ['sun', 'betelgeuse']

'''
Triple quotes
Multi-line strings
'''
stars = ['sun', 'betelgeuse']


def double(num):
  '''Double the value'''
  return 2*num

print(double(sum))