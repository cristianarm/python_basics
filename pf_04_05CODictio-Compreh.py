# Comprehension lists
print('\n ---- Comprehension lists  ------')

powers = [2, 4, 8, 16, 32]
pw=[x**3 for x in powers]
print(pw)


authors = ['Carl', 'King', 'Neil', 'Klauss']
print(['Author '+ a for a in authors if a[0] == 'K'])

books = ['IT', 'Cosmo', 'Black Holes', 'Whoville']
print([b + ' len '+ str(len(b)) for b in books if len(b) > 5])