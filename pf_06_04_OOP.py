print('\n ---- Using Class Bird  ------')

from pf_06_03_OOP import Bird

class Penguin(Bird):
    def __init__(self, name):
        #super().__init__(self, name)
        #super(self.name)
        Bird.__init__(self, name)
        self.species = 'penguin'
        self.fly     = False
        self.swim    = True

    def canSwim(self):
        return self.swim


pingu = Penguin('Pingu')
print('{} is a {}'.format(pingu.name, pingu.whoisThis()))
print('{} can swim? {}'.format(pingu.name, pingu.canSwim()))