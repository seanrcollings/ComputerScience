class Account(object):
    def __init__(self, _id=None, balance=None, annualtInterestRate=1):
        self.__id = _id
        self.__balance = balance
        self.__annualtInterestRate = annualtInterestRate / 100
        self.__monthlyInterestRate = self.__annualtInterestRate / 12

    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualtInterestRate

    def getMonthlyInterestRate(self):
        return self.__monthlyInterestRate

    def getMonthlyInterest(self):
        return self.__balance * self.__monthlyInterestRate
         
    def setId(self, newId):
        if newId >= 0:
            self.__id = newId
            return True
        return False

    def setBalance(self, newBalance):
        if newBalance >= 0:
            self.__balance = newBalance
            return True
        return False

    def setAnnualInterestRate(self, newAnnualInterestRate):
        if newAnnualInterestRate <= 10 and newAnnualInterestRate >= 0:
            self.__annualtInterestRate = newAnnualInterestRate / 100
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.__balance - amount >= 0:
            self.__balance -= amount
            return True
        print("You tried to withdraw more money than was in your account, or tried to withdraw a negative amount of money")
        return False

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        print("You tried to deposit a negative amount of money")
        return False

