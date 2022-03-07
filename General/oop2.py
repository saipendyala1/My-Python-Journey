
# # In python, classes are used:
# # • as a template to create instances (or objects) of that class,
# # • define attributes or fields to hold data within the objects,
# # • define instance methods or common behaviour for a class of objects,

# # # Objects (or instances) on the other hand can:
# # • be created from a class,
# # • hold their own values for instance variables,
# # • execute instance methods,
# # • may have many copies in the system (all with their own data).

# # format of class defintion in Python
# class NameOfClass(SuperClass):
#     __init__
#     attributes
#     methods

 

# Define an Account class
class Account():
    pass

# instantiate (create) an object of Account class
a1 = Account()
print(a1)


""" class Account(object):

    def balance(self):
        pass

    def withdraw(self, amount): 
        pass

    def deposit(self, amount): 
        pass

    def transfer(self, target, amount): 
        pass 


a1 = Account()
print(a1)

a1.deposit(1000)
a1.transfer(2078987, 1200.87)

# no way of storing and changing the values
"""


# class Account(object):

#     # special method called __init__
#     # initialiser (constructor) for the class
#     # class attributes - indicates what data must be supplied when the class is created 
#     def __init__(self, holder, number, balance, credit_line=1500): 
#         self.Holder = holder 
#         self.Number = number 
#         self.Balance = balance
#         self.CreditLine = credit_line
    
#     def sayHello(self):
#         print("Hello: ", self.Holder)

# a1 = Account("Bob", 202101, 2500)
# a1.sayHello()



# from datetime import date

# class Account(object):

#     # init method
#     def __init__(self, holder, number, balance, credit_line=1500): 
#         self.Holder = holder 
#         self.Number = number 
#         self.Balance = balance
#         self.CreditLine = credit_line
    
#     def sayHello(self):
#         print("Hello: ", self.Holder)
    
#     def balance(self):
#         print("Your balance is {}".format(self.Balance))
#         return self.Balance
    

# a1 = Account("Bob", 202101, 2500)
# a1.sayHello()
# a1.balance()


# from datetime import date
# class Account(object):

#     # init method
#     def __init__(self, holder, number, balance, credit_line=1500): 
#         self.Holder = holder 
#         self.Number = number 
#         self.Balance = balance
#         self.CreditLine = credit_line
    
#     def sayHello(self):
#         print("Hello: ", self.Holder)
    
#     def balance(self):
#         print("Your balance is {}".format(self.Balance))
#         return self.Balance
    
#     def deposit(self, amount):
#         self.Balance += amount
#         print("You deposited an amount of {} on {}".format(amount, date.today()))
#         print("Your total balance is {}".format(self.Balance))

    
# a1 = Account("Bob", 202101, 2500)
# #a1.sayHello()
# #a1.balance()
# a1.deposit(500)


# from datetime import date
# class Account(object):

#     # init method
#     def __init__(self, holder, number, balance, credit_line=1500): 
#         self.Holder = holder 
#         self.Number = number 
#         self.Balance = balance
#         self.CreditLine = credit_line
    
#     def sayHello(self):
#         print("Hello: ", self.Holder)
    
#     def balance(self):
#         print("Your balance is {}".format(self.Balance))
#         return self.Balance
    
#     def deposit(self, amount):
#         self.Balance += amount
#         print("You deposited an amount of {} on {}".format(amount, date.today()))
#         print("Your total balance is {}".format(self.Balance))
    
#     def withdraw(self, amount): 
#         if(self.Balance - amount < -self.CreditLine):
#             # coverage insufficient
#             print("You have insufficient balance. Your current balance is {}".format(self.Balance))
#             return False  
#         else: 
#             self.Balance -= amount
#             print("Your balance after withdrawl is {}".format(self.Balance))
#             return True
    

# a1 = Account("Bob", 202101, 2500)
# #a1.sayHello()
# #a1.balance()
# #a1.deposit(500)
# a1.withdraw(5000)


# from datetime import date
# class Account(object):

#     # init method
#     def __init__(self, holder, number, balance, credit_line=1500): 
#         self.Holder = holder 
#         self.Number = number 
#         self.Balance = balance
#         self.CreditLine = credit_line
    
#     def sayHello(self):
#         print("Hello: ", self.Holder)
    
#     def balance(self):
#         print("Balance: {}".format(self.Balance))
#         return self.Balance
    
#     def deposit(self, amount):
#         self.Balance += amount
#         print("Deposited: {} on {}".format(amount, date.today()))
#         print("Total Balance: {}".format(self.Balance))
    
#     def withdraw(self, amount): 
#         if(self.Balance - amount < -self.CreditLine):
#             # coverage insufficient
#             print("Insufficient balance. Your current balance: {}".format(self.Balance))
#             return False  
#         else: 
#             self.Balance -= amount
#             print("Your balance after withdrawl is {}".format(self.Balance))
#             return True
    
#     def transfer(self, target, amount):
#         if(self.Balance - amount < -self.CreditLine):
#             # coverage insufficient
#             return False
#         else: 
#             self.Balance -= amount 
#             target.Balance += amount 
#             return True


# a1 = Account("Bob", 202101, 2500)
# #a1.sayHello()
# #a1.balance()
# #a1.deposit(500)
# #a1.withdraw(5000)
# a2 = Account("Sam", 202101, 1500)

# a1.transfer(a2, 500)
# a2.balance()

""" 
# Data Encapsulation
from datetime import date
class Account(object):

    # init method
    def __init__(self, holder, number, balance, credit_line=1500): 
        self.__Holder = holder 
        self.__Number = number 
        self.__Balance = balance
        self.__CreditLine = credit_line
    
    def sayHello(self):
        print("Hello: ", self.__Holder)
    
    def balance(self):
        print("Balance: {}".format(self.__Balance))
        return self.__Balance
    
    def deposit(self, amount):
        self.__Balance += amount
        print("Deposited: {} on {}".format(amount, date.today()))
        print("Total Balance: {}".format(self.__Balance))
    
    def withdraw(self, amount): 
        if(self.__Balance - amount < -self.__CreditLine):
            # coverage insufficient
            print("Insufficient balance. Your current balance: {}".format(self.__Balance))
            return False  
        else: 
            self.__Balance -= amount
            print("Your balance after withdrawl is {}".format(self.__Balance))
            return True
    
    def transfer(self, target, amount):
        if(self.__Balance - amount < -self.__CreditLine):
            # coverage insufficient
            return False
        else: 
            self.__Balance -= amount 
            target.__Balance += amount 
            return True


a1 = Account("Bob", 202101, 2500)
#a1.sayHello()
#a1.balance()
#a1.deposit(500)
#a1.withdraw(5000)
a2 = Account("Sam", 202101, 1500)

a2.balance()
a1.withdraw(500)
 """

