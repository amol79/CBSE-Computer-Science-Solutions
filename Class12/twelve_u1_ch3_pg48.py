class Mobile:
  '"A sample class definition"'
  price = 0
  model = "Null"
  def __init__(self, price, model = None):
    self.price=price
    self.model=model 
  
  def displayData(self, ):
    print("Details of Mobile are: ", self. price, self. model)

  def displayClassData():
    print("Details of class variables are:", Mobile.price, Mobile.model)

  def dictionaryFunctions(self, ):
    print("calling vars() function:")
    print(vars(self))
    print("calling dir() function:")
    print(dir(self))  

M1 = Mobile(10000, "Redmi Note 3")
M2 = Mobile(15000, "Realme 2 Pro")
M1.displayData()
M2.displayData()
Mobile.displayClassData()
M1.dictionaryFunctions()
M2.dictionaryFunctions()

"""
Python 3.7.4 (default, Jul  9 2019, 00:06:43)
[GCC 6.3.0 20170516] on linux
Details of Mobile are:  10000 Redmi Note 3
Details of Mobile are:  15000 Realme 2 Pro
Details of class variables are: 0 Null
calling vars() function:
{'price': 10000, 'model': 'Redmi Note 3'}
calling dir() function:
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__','__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'dictionaryFunctions', 'displayClassData', 'displayData', 'model', 'price']
calling vars() function:
{'price': 15000, 'model': 'Realme 2 Pro'}
calling dir() function:
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__','__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'dictionaryFunctions', 'displayClassData', 'displayData', 'model', 'price']
"""
