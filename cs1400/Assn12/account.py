class Account(object):
    def __init__(self, _id, balance, annualtInterestRate):
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
        self.__id = newId

    def setBalance(self, newBalance):
        self.__balance = balance

    def setAnnualInterestRate(self, newAnnualInterestRate):
        self.__annualtInterestRate = newAnnualInterestRate

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

