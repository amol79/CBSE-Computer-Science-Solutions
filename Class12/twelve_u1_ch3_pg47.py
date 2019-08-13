class Mobile:
  '"A sample class definition"'
  price = 0
  model = "Null"
  def __init__(self, price, model = None):
    self.price=price
    self.model=model
  
  def displaydata(self, ):
    print("Details of Mobile are: ", self. price, self. model)

M1 = Mobile(10000, "Redmi Note 3")
M1.displaydata()

M2 = Mobile(15000, "Realme 2 Pro")
M2.displaydata()

"""
Python 3.7.4 (default, Jul  9 2019, 00:06:43)
[GCC 6.3.0 20170516] on linux
Details of Mobile are:  10000 Redmi Note 3
Details of Mobile are:  15000 Realme 2 Pro
"""
