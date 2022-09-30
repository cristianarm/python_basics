# Strings

print('\n ---- Strings  ------')

s1 = 'The white fox'
print('* like list')
print("String: " + s1)
print(s1[0]) 
print(s1[-3]) 
print(s1[4:10])
print(s1[10:4])
print(len(s1))

#s1[0] = 't'
#  TypeError: 's1' object does not support item assignment

print('* join strings')
print(s1 +' '+ str(39))
print("My friend {1} likes go to party with {0} and {2}".format('John','Pepe','Lee'))
print('La edad de {name} ->  es de {age}'.format(name='Pepito', age=3))