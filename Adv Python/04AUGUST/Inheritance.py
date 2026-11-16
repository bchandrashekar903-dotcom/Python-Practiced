'''             Inheritance             '''

'''                   Single Inheritance                 '''
# class Bitm:
#     def fee(self):
#         print("College fee is 45000")

# class College(Bitm):
#     def due(self):
#         print("Due is 10000")

# c = College()
# c.fee()
# c.due()

'''                     Multilevel inheritance                  '''
#   class Parent:
#     def fun1(self):
#         print("Function 1 is Parent Class  ")

# class Child(Parent):
#     def fun2(self):
#         print("Function 2")

# class Grandchild(Child):
#     def fun3(self):
#         print("Function 3")

# g = Grandchild()
# g.fun1()
# g.fun2()
# g.fun3()


'''          Hierarchical inheritance              '''
# class Parent:
#     def fun1(self):
#         print("Parent class")

# class Child1(Parent):
#     def fun2(self):
#         print("Child 1 class")

# class Child2(Parent):
#     def fun3(self):
#         print("Child 2 class")

# c2= Child2()
# c2.fun3() 

# c1 = Child1()
# c1.fun2()

'''              Multiple inheritance                  '''
# class Father:
#     fathername = ""
#     def father(self):
#         print(self.fathername)

# class Mother:
#     mothername = ""
#     def mother(self):
#        print(self.mothername)

# class Son(Father,Mother):
#     def parents(self):
#         print("Father is ",self.fathername)
#         print("Mother is ",self.mothername)
# s1 = Son()
# s1.fathername = "Raj"
# s1.mothername = "Srav"
# s1.parents()

'''              Hybrid inheritance              '''











'''Create a class called savings accont where previosly we have bank 
account wherer attributes are accno and balance now additionally in 
savings account you have one more function called interest rate of 5% '''

class BankAcc:
    def __init__(self,acc_no,bal):
        self.acc_no = acc_no
        self.bal = bal

    def disp(self):
        print(f"Account number:{self.acc_no}")
        print(f"Balance: {self.bal}")

class SavingsAcc(BankAcc):
    def __init__(self,acc_no,bal):
        super().__init__(acc_no,bal)
        self.interest_rate =  0.05
    
    def calculate_interest(self):
        interest = self.bal*self.interest_rate
        return interest

Msa = SavingsAcc("123",5000)
Msa.disp()
print("Interest (5%):",Msa.calculate_interest())





        
    

