class Mobile:
  '"A sample class definition"'
  price = 0 #class variable
  model = "Null" #class variable
  def __init__(self, price, model = None):
    self.price=price #object variables
    self.model=model 
  
  def displayData(self, ):
    print("Details of Mobile are: ", self. price, self. model) #object variables

  def displayClassData():
    print("Details of class variables are:", Mobile.price, Mobile.model) #class variables

M1 = Mobile(10000, "Redmi Note 3")
M2 = Mobile(15000, "Realme 2 Pro")
M1.displayData()
M2.displayData()
Mobile.displayClassData()

"""
Python 3.7.4 (default, Jul  9 2019, 00:06:43)
[GCC 6.3.0 20170516] on linux
Details of Mobile are:  10000 Redmi Note 3
Details of Mobile are:  15000 Realme 2 Pro
Details of class variables are: 0 Null
"""
