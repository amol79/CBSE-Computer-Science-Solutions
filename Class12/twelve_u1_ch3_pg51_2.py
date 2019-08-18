class Health_Profile():
  weight = 60
  height = 170

  def __init__(self, name, weight, height):
    self.name = name
    self.weight = weight
    self.height = height

#We want all instances of Health_Profile to have the displayProfile method
def displayProfile(self):
  print("Welcome", self.name)
  print("Your weight is: ", self.weight)
  print("Your Height is: ", self.height)

#we will assign displayProfile method to some attribute of class Health_Profile
Health_Profile.display = displayProfile #here use only method name, no brackets
H1 = Health_Profile("Amol", 62, 170)
H2 = Health_Profile("Aman", 78, 180)
H1.display()
H2.display()

"""
Output:
Welcome Amol
Your weight is:  62
Your Height is:  170
Welcome Aman
Your weight is:  78
Your Height is:  180
"""
