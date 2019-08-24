class person(object): #base class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class student(person): #derived class
    def __init__(self, name, age, rollno, marks):
        self.rollno = rollno
        self.marks = marks
        super().__init__(name, age) 
        #in python 2.x syntax is super(type(variable), variable).__init__()
        #another option is to call using name of super class like
        """
        person.__init__(self, name, age)
        """
        #but calling using super() is better as even if mapping of base class changes, super() reference will automatically follow

    def getRoll(self):
        return self.rollno

    def getMarks(self):
        return self.marks


if __name__ == "__main__":
    s1 = student("Aman", 23, 24, 88)
    print("Name: ", s1.getName())
    print("Age: ", s1.getAge())
    print("Roll no: ", s1.getRoll())
    print("Marks: ", s1.getMarks())

"""
Output:
Name:  Aman
Age:  23
Roll no:  24
Marks:  88
"""
