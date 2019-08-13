class Initialize:
  var = 0

  def __init__(self, var=10): #double underscore before and    after init
    Initialize.var=var
    #self.var = var #also valid

  def display(some_random_name):
    print("Output using some_random_name ", some_random_name.var)
    #print("Output using self.var:", self.var) 
    #will give error 'self' is not defined

P = Initialize(20)
P.display()

"""
Output:
Python 3.7.4 (default, Jul  9 2019, 00:06:43)
[GCC 6.3.0 20170516] on linux
Output using some_random_name  20
"""
