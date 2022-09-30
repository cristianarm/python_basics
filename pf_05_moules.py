print('\n ---- Modules  ------')
# Add two lists using map and lambda
from math import factorial as fact

numbers1 = [23, 12, 2]

numbers2 = [fact(x) for x in numbers1 ]
print(numbers1,'\n',numbers2)
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))
  
