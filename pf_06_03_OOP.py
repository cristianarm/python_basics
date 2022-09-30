# Classes
# class Bird

class Bird:

    species = 'bird'
    fly     = True

    def __init__(self, name):
        print("Bird is ready")
        self.name = name

    def whoisThis(self):
        return self.species

    def canFly(self):
        return self.fly