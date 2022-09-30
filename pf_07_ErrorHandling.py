print('\n ---- Error Handling ------')

print('Generate Error')
#print(10 * (1/0))
# ZeroDivisionError: division by zero

#print(4 + spam*3)
# NameError: name 'spam' is not defined

#print('2' + 2.4666)
# TypeError: can only concatenate str (not "int") to str

def limited_division(x, y):
  try:
    print( "x= ", x, "y= ", y)
    if y >= x:
      raise ValueError('Error: '+ str(y) + ' must be greater than ' + str(x))

    result = x / y

  except ZeroDivisionError:
    print('Cannot divide by 0')
  except ValueError as e:
    print(e)
  else:
    print('Division result is: {}'.format(result))
  finally:
    print('This is executed no matter what')

limited_division(2, 1)
limited_division(10, 0)
limited_division(3, 5)