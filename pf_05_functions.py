print('\n ---- functions  ------')

def factorial(n=0):
    '''Computes the factorial of an integer "n"'''
    if n < 0:
        raise ValueError('Number must be non-negative')
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print('\ncall the function')
print('without params ',factorial())
print('with params ',factorial(13))

fruits = ['orange', 'strawberry', 'apple']
print('\n ---- lambda  ------')
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('austin', 'powers'))

print((lambda x, y: x * y)(44, 33))