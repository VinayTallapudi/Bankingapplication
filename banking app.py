from abc import ABC,abstractmethod
import sys
from random import*
def accnumber():
    digits='0123456789'
    accnu=''
    for i in range(12):
        accnu=accnu+choice(digits)
    return accnu
class Account(ABC):
    bankname='TCC Corp'
    statement=[]
    tcount=0
    def __init__(self,name,accnum,bal):
        self.name=name
        self.accnum=accnumber()
        self.bal=bal
    def _deposit(self,amt):
        self.bal=self.bal+amt
        print('avail balance:',self.bal)
        Account.statement.append('Amount credited {} : updated balance {}'. format(amt,self.bal))
    def _withdraw(self,amt,min_bal):
        while Account.tcount>5:
            print('Your max number of attemapts reached {}, please try after 24hrs'. format(self.name))
            sys.exit()
        if amt%100!=0:
            print("Please enter amount only in multiples of '100'")
        elif(amt>self.bal):
            print('Insufficient funds :')
        elif (self.bal-amt)<min_bal:
            print('Balance cannot be less than minimun balance, please transact maintaining minimun balance amount')
        else:
            self.bal=self.bal-amt
            print('money dispensed sucessfully')
            print('avail balance:',self.bal)
            Account.statement.append('Amount debited {} : updated balance {}'. format(amt,self.bal))
            Account.tcount+=1
    @abstractmethod
    def balenquiry(self):
        pass
    @abstractmethod
    def getaccountinfo(self):
        pass
    def _history(self):
        print('---*-STATEMENT-*---')
        for transaction in Account.statement:
            print(transaction)       
class Savingsaccount(Account):
    def __init__(self,name):
        super().__init__(name,accnum='',bal=0)
    def deposit(self):
        try:
            amt=abs(float(input('Enter deposit money:')))
            self._deposit(amt)
        except ValueError:
            print('Please Enter amount in numbers only')
    def withdraw(self):
        try:
            amt=abs(float(input('Enter withdrawl amount:')))
            while amt<=0 or amt>10000:
                print('Please do not exceed Transaction limit')
                amt=abs(float(input('enter Withdrawl amout:')))
            self._withdraw(amt,0)
        except ValueError:
            print('Please Enter amount in numbers only')
    def balenquiry(self):
        print('Balance in your savings acconut with acc num xxxxxxxxx{} is {} rs.'. format(self.accnum[9:],self.bal))
    def getaccountinfo(self):
        print('Name : ',self.name)
        print('Accout Number : ',self.accnum)
        print('Account type : Savings Account')
    def history(self):
        self._history()
class Currentaccount(Account):
    def __init__(self,name):
        super().__init__(name,accnum='',bal=0,)
    def deposit(self):
        try:
            amt=abs(float(input('Enter deposit amount:')))
            self._deposit(amt)
        except:
            print('Please Enter amount in numbers only')
    def withdraw(self):
        amt=abs(float(input('Enter Withdrawl money:')))
        while amt==0 or amt>10000:
            print('Please do not exceed Transaction limit')
            amt=abs(float(input('Enter Withdrawl amount:')))
        self._withdraw(amt,1000)
    def balenquiry(self):
        print('Balance in your current acconut with acc num xxxxxxxxx{} is {} rs.'. format(self.accnum[9:],self.bal))
    def getaccountinfo(self):
        print('Name : ',self.name)
        print('Accout Number : ',self.accnum)
        print('Account type : Current Account')
    def history(self):
        self._history()
print('Welcome to,',Account.bankname)
print('The page you are viewing is to create an account in {}, please follow the instructions'. format(Account.bankname))
name=input('Enter your name:')
print('S - Savings account\nC - Current account')
option=input('Enter your option from above : ').lower()
while option not in ['s','c']:
    option=input('Please enter a valid option from S or C :')
if option=='s':
    a=Savingsaccount(name)
    print('Account number :',a.accnum)
else:
    a=Currentaccount(name)
    print('Account number :',a.accnum)
while True:
    print('D : deposit\nW : withdrawl\nB : balance enquiry\nS : Statement\ni : Account info\nE : exit transaction')
    option=input('Choose any option:').lower()
    while option not in ('d','w','b','s','i','e'):
        option=input('Please choose valid option from above : ').lower() 
    if option=='d':
        a.deposit()
        print('Money deposited sucessfully')
    elif option=='w':
        a.withdraw()
    elif option=='b':
        a.balenquiry()
    elif option=='i':
        a.getaccountinfo()
    elif option=='s':
        a.history()
    elif option=='e':
        print('terminating...')
        print('Thankyou,', a.name)
        sys.exit()




       
        

        
    
    
            
    
    
        
