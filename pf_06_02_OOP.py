print('\n ---- Using Class Parrot  ------')

from pf_06_01_OOP import Parrot

# instantiate the Parrot class
blu = Parrot("Blu", 8)
woo = Parrot(name="Woo", age=15)

# access the class attributes
print("# access the class attributes")
print("Blu is a {}".format(blu.__class__.species))
print("A parrot is a {}".format(Parrot.species))

# access the instance attributes
print("# access the instance attributes")
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))

# call the methods
print("# call the methods")
print(woo.sing("Lambada"))
print(blu.secret())
print(Parrot.isAdult(22))
print(blu.isAdult(22))
