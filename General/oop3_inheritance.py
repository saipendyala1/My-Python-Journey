from datetime import date
class Account(object):

    # init method
    def __init__(self, holder, number, balance, credit_line=1500): 
        self.holder = holder 
        self.number = number 
        self.balance = balance
        self.creditLine = credit_line
    
    def sayHello(self):
        print("Hello: ", self.holder)
    
    def showBalance(self):
        print("Balance: {}".format(self.balance))
        return self.Balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposited: {} on {}".format(amount, date.today()))
        print("Total Balance: {}".format(self.balance))
    
    def withdraw(self, amount): 
        if(self.balance - amount < -self.creditLine):
            # coverage insufficient
            print("Insufficient balance. Your current balance: {}".format(self.balance))
            return False  
        else: 
            self.balance -= amount
            print("Your balance after withdrawl is {}".format(self.balance))
            return True
    
    def transfer(self, target, amount):
        if(self.balance - amount < -self.creditLine):
            # coverage insufficient
            return False
        else: 
            self.balance -= amount 
            target.balance += amount 
            return True


a1 = Account("Bob", 202101, 2500)
a2 = Account("Sam", 202101, 1500)

# A bank account that charges for withdrawals.
class CheckingAccount(Account):

    withdraw_charge = 1

    # init method
    def __init__(self, holder, number, balance, credit_line=1500):
        super().__init__(holder, number, balance)
        
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)


c1 = CheckingAccount('Tom', 2021102, 1000)
print(c1.holder)
c1.withdraw(50)
c1.deposit(50)
c1.showBalance



