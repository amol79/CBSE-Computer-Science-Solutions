class Health_Profile():
  weight = 60
  height = 170

  def __init__(self,name):
    self.name = name

def displayProfile():
  print("Welcome")
  
H1 = Health_Profile('Patient1')
H1.disp = displayProfile #here we are creating a new attribute for H1 called disp.
#disp is pointing to the displayProfile function
H1.disp()

"""
output:
Welcome
"""
