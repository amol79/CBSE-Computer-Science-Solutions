from types import MethodType

class Health_Profile():
  weight = 0
  height = 0

  def __init__(self, name):
    self.name = name

def displayProfile(self):
  print("Welcome ", self.name)
  print("Weight: ", self.weight)
  print("height: ", self.height)

h1 = Health_Profile("Amol")
h1.display = displayProfile
h1.display(h1)

setattr(h1,"weight", 62)
setattr(h1,"height",170)

print("The Weight after setattr: ", getattr(h1,"weight"))
print("The Height after setattr: ", getattr(h1,"height"))

print("Check hasattr: ",hasattr(h1,"name"))

print("Before deleting weight: ", vars(h1))
delattr(h1,"weight")
print("After deleting weight: ", vars(h1))

"""
Output:
Python 3.7.4 (default, Jul  9 2019, 00:06:43)
[GCC 6.3.0 20170516] on linux
Welcome  Amol
Weight:  0
height:  0
The Weight after setattr:  62
The Height after setattr:  170
Check hasattr:  True
Before deleting weight:  {'name': 'Amol', 'display': <function displayProfile at 0x7f78bcc193b0>, 'weight': 62, 'height': 170}
After deleting weight:  {'name': 'Amol', 'display': <function displayProfile at 0x7f78bcc193b0>, 'height': 170}
"""
