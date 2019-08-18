from types import MethodType

class Health_Profile():
  weight = 60
  height = 170

  def __init__(self, name):
    self.name = name

#this is the function which will be dynamically assigned to object of class Health_Profile
def displayProfile(self):
  print("Welcome", self.name)
  print("Your weight is: ", self.weight)
  print("Your Height is: ", self.height)

H1 = Health_Profile("Amol")
H1.display = MethodType(displayProfile, H1)
#here we are binding displayProfile method to H1 object
#only H1 object will have the displayProfile method, other objects wont have
H1.display()

"""
Output:
Python 3.7.4 (default, Jul  9 2019, 00:06:43)
[GCC 6.3.0 20170516] on linux
Welcome Amol
Your weight is:  60
Your Height is:  170
"""

#reference link: http://igorsobreira.com/2011/02/06/adding-methods-dynamically-in-python.html
