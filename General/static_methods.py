#class methods vs. static methods

# class method

#class C(object):
#    @classmethod
#    def fun(cls, arg1, arg2, ...):
#       ....
#fun: function that needs to be converted into a class method
#returns: a class method for function.

# A class method is bound to the class and not the object of the class.
# They have the access to the state of the class as it takes a class parameter 
# that points to the class and not the object instance.
# It can modify a class state that would apply across all the instances of the class. 
# For example it can modify a class variable that will be applicable to all the instances.

# static method

#class C(object):
#    @staticmethod
#    def fun(arg1, arg2, ...):
#        ...
#returns: a static method for function fun

# A static method is also a method which is bound 
# to the class and not the object of the class.
# A static method can’t access or modify class state.

# Class methods are generally used to create factory methods. 
# Factory methods return class object ( similar to a constructor ) for different use cases.
# We generally use static methods to create utility functions.
# Utility functions are set of mhthods that perform common, often reused functions


# Python program to demonstrate  
# use of class method and static method. 
from datetime import date 
   
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
       
    # a class method to create a Person object by birth year. 
    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
       
    # a static method to check if a Person is adult or not. 
    @staticmethod
    def isAdult(age): 
        return age > 18
    
    def __str__(self):
        return "{self.name} is {self.age} years old".format(self=self)


person1 = Person('John', 45) 
print (person1.age)
print(person1)

person2 = Person.fromBirthYear('Jim', 1985) 
print (person2.age)
print(person2)
   
# print the result 
print (Person.isAdult(22))