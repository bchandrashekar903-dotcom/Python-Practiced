'''Create a class called savings accont where previosly we have bank 
account wherer attributes are accno and balance now additionally in 
savings account you have one more function called interest rate of 5% '''
 
class Bank_Acc:
    def __init__(self,acc_no,bal):
        self.acc_no = acc_no
        self.bal = bal 

    def debit(self,amount):
        if amount>self.bal:
            print("Insufficient Balance")
        self.bal -= amount
        print(f"Amount has been deducted {amount}")
        print(f"The updated balance is {self.getbal()}")

    def credit(self,amount):
        self.bal += amount
        print(f"Amount has been added to the account {amount}")
        print(f"The updated balance is {self.getbal()}")
 
    def getbal(self):
        return self.bal

class Savings(Bank_Acc):
    def __init__(self,interest_rate):
        super().__init__(123,1000)
        self.interest_rate = interest_rate
    
    def cal_interest(self):
        interest = self.bal*(self.interest_rate/100)
        self.bal+=interest
        print(self.getbal())
    
s = Savings(5)
s.cal_interest()
s.credit(5000)
s.debit(550)