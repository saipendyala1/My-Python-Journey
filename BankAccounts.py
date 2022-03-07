# Student Name: Saiteja Pendyala Student Id:201538148.

# Define class Basic Account
class BasicAccount:

    """
    BasicAccount is a type of Bankaccount and has acName, amount
    """
    # The Account Number of the Bank Account
    acNum = 0
    # Define the initialiser
    def __init__(self, theacName, amount):
        self.acName = theacName
        self.balance = amount
        BasicAccount.acNum += 1
        print("Account Name: {self.acName}, Opening Balance: £{self.balance}.".format(self=self))

    def __str__(self):
        return 'Account Name:{self.acName}, Available Balance: £{self.balance}'.format(self=self)


  # Define Methods
    def deposit(self, amount):
        """
        Deposits the stated amount into the account, and adjusts the balance appropriately.

        Parameters:
            amount
        Returns:
            Nothing
        """
        if(amount>0):
             self.balance += amount
        else:
            ("please, enter valid amount!")

    def withdraw(self,amount):
        """
        Withdraws the stated amount from the account

        Parameters:
            amount
        Returns:
            Nothing
        """
        if(self.balance - amount < 0):
            print("Can not withdraw £" + amount)
        else:
            self.balance -= amount
            print(self.acName + " has withdrew £" + str(amount) + ". New balance is £" + str(self.balance))

    def getAvailableBalance(self):
        """
        Returns the total balance that is available in the account.
        
        Parameters:
            None
        Returns:
            Nothing
        """
        return 'Total Balance: £{self.balance}'.format(self = self)

    def getBalance(self):
        """
        returns the balance of the account.

        Parameters:
            None
        Returns:
            balance
        """
        if (self.balance<0):
            return '-{self.balance}'.format(self = self)
        else:
            return 'Balance: £{self.balance}'.format(self = self)
    def printBalance(self):
        """
        prints balance of the account.

        Parameters:
            None
        Returns:
            Nothing
        """
        print("Balance: £{self.balance}".format(self = self))
    def getName(self):
        """
        Returns the name of the account holder.

        Parameters:
            None
        Returns:
            Name of the Account Holder
           
        """
        return'Name of the Account Holder: {self.acName}'.format(self = self)

    def getAcNum(self):
        """
        Returns the account number as a string

        Parameters:
            None
        Returns:
            Number of the Account Holder
        """
        return str(BasicAccount.acNum)

    def issueNewCard(self):
        """
        Creates a new card number with the expiry.

        Parameters:
            None
        Returns:
            CardNumber and Card Expiry
        """
        from random import randint
        CardNum = ''
        for i in range(16):
            CardNum = CardNum + str(randint(0,9))

        import datetime
        now = (datetime.datetime.now())
        year = str(now.year)[-2:]
        y = int(year)+3
        cardExp =  (now.month, y)
        return CardNum, cardExp
    def closeAccount(self):
        """
        Returns any balance to the customer.
        
        Parameters:
            None
        Returns:
            Boolean
        """
        if(self.balance >= 0):
            self.withdraw(self.balance)
            return True
        else:
            print("Can not close account due to customer being overdrawn by" + self.balance )
            return False

# Define class Premium Account
class PremiumAccount(BasicAccount):
    # Define the initialiser
    def __init__(self, theacName, amount, theinitialOverdraft):
        super().__init__(theacName, amount)
        self.initialOverdraft = theinitialOverdraft
    
    def __str__(self):
        return 'Account Name:{self.acName}, Available Balance: £{self.balance}'.format(self=self)
 # Define Methods
    def setOverdraftLimit(self, thenewlimit):
        """
        Sets the overdraft limit to the stated amount.

        Parameters:
            thenewlimit
        Returns:
            None
        """
        self.newlimit = thenewlimit
    def getAvailableBalance(self, amount):
        """
        Returns the total balance that is available in the account.

        Parameters:
            amount
        Returns:
            total balance
        """
        return'total balance: {self.balance} overdraft: {self.newlimit}'.format(self = self)
    def printBalance(self):
        """
        prints the balance of the account.
        
        Parameters:
            None
        Returns:
            Nothing
        """
        print("the balance of the account: {self.balance} overdraft: {self.newlimit}".format(self = self))

        