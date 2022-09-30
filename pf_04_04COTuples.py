# Tuples
print('\n ---- Tuples  ------')

noble_gases = ('helium', 'xenon', [2, 4])
print('* print one item')
print(noble_gases[0])
print(noble_gases[-1])
print('* print multi item')
print(noble_gases[1:])
print(noble_gases[0:])

print('\n* manipulate Tuples')
#noble_gases[0] = 'argon'
# TypeError: 'tuple' object does not support item

print(noble_gases[2])
noble_gases[2][0] = 10
noble_gases[2].append(98)
# noble_gases[2].append = 98
# AttributeError: 'list' object attribute 'append' is read-only
print(noble_gases[2])
print(noble_gases[:])
print(noble_gases + ('argon', 'krypton'))


#sets
print('\n ---- Sets  ------')
snoble_gases = {'helium', 'xenon', 'neon'}
print(snoble_gases)
snoble_gases.add('argon')
print(snoble_gases)
snoble_gases.add('Radon')
print(snoble_gases)
snoble_gases.update({'argon','krypton','Diamantina'})
print(snoble_gases)
snoble_gases.remove('helium')
print('helium' in snoble_gases)
print('krypton' in snoble_gases)
test= snoble_gases.union({'radon', 'Amatista'})
print(test)