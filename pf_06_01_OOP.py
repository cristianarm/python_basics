# Classes
# Class Parrot
class Parrot:

  # class attribute
  species = "bird"

  # initializer
  def __init__(self, name, age):
    self.name    = name
    self.age     = age
    self._secret = "It loves cookies"

  # instance method
  def sing(self, song):
    return "{} sings {}".format(self.name, song)

  def secret(self):
    return "{} secret: {}".format(self.name, self._secret)

  @staticmethod
  def isAdult(age):
    return age > 10