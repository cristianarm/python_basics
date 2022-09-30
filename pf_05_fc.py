print('\n ---- Flow Control  ------')

print('\nif/else')
a, b = 33, 40
if b > a:
    print("b is greater than a")
elif b < a:
    print("b is less than a")
else:
    print("a and b are equal")


fruits = ['orange', 'strawberry', 'apple']
print('\n*  for loop')

for fruit in fruits: 
    print("Fruit: ",fruit)

# for loop + enumerate
for poss, value in enumerate(fruits):
 print("Pos:",str(poss) +", Valor: "+ value)

# for loop + range() + else
sum = 0
for x in range(16):
    print("Value x: ",x)
    if x % 2 == 0:
        sum += x
    else:
        print("Sum is {0}".format(sum))

print('\n*  while loop')
power = 1
while True:
    if power >= 1024:
        break
    power *= 2
print("Power is {0}".format(power))