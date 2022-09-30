# Lists
print('\n ---- List  ------')
stars=['antares', 'capella', 'sirius','situla','talitha']
print('* print one item')
print(stars[0])
print(stars[-1])
print('* print multi item')
print("[:] : " , stars[:])
print("[0:2] : " , stars[0:2])
print("[1:] : " , stars[1:])
print("[:1] : " , stars[:1])
print("[-1:1] : " , stars[-1:1])
print("[1:-1] : " , stars[1:-1])

print('\n* manipulate list')
stars[0] = 'vega'
print(stars[0])
#stars[5] = 'polaris'
# IndexError: list assignment index out of range
print("\n* -- Add value to list")
stars.append('polaris')
print(stars[5])
print(stars[-1])
print("without order" , stars[:])
stars.sort()
print("with sort" , stars[:])
stars3 = stars + ['sun']
print(stars + ['sun'])
print(stars3[:])