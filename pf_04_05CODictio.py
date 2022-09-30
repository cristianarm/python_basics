# Dictionaries
print('\n ---- Dictionaries  ------')
author = {'name': 'Carl', 'age': 47}
print(author['name'])
print(list(author.keys()))

for key, value in author.items():
  print('(llave){0}: {1} (Valor)'.format(key, value))


other_author = author
other_author['name'] = 'Juan'
other_author['age'] = 30
print(other_author['name'])
print(other_author['age'])

for key, value in author.items():
  print('{0}: {1}'.format(key, value))


other_author = author.copy()
other_author['name'] = 'Peter'
other_author['age'] = 88
print(other_author['name'])
print(other_author['age'])

for key, value in author.items():
  print('{0}: {1}'.format(key, value))