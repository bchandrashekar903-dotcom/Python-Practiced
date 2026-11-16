'''  Create a class for bank account where we have functions to do those are
debit and credit and you need to return one of the employee's account
balance after performing the debit and credit transactions where the 
parameters of bank account are balance and account_no  '''


# class Bank_Acc:
#     def __init__(self,acc_no,bal):
#         self.acc_no = acc_no
#         self.bal = bal 

#     def debit(self,amount):
#         self.bal -= amount
#         print(f"Amount has been deducted {amount}")
#         print(f"The updated balance is {self.getbal()}")

#     def credit(self,amount):
#         self.bal += amount
#         print(f"Amount has been added to the account {amount}")
#         print(f"The updated balance is {self.getbal()}")
 
#     def getbal(self):
#         return self.bal

# acc = Bank_Acc(12321,10000)
# acc.debit(500)
# acc.credit(1000)



# # Types of methods
# #   1. Instance
# #   2. Static Method
# #   3. Class Method

# # Example for static method 
# # Statci method cannot have any parameters to be passed into the method

# class Bitm:
#     @staticmethod
#     def func():
#         print("Hello")
# b = Bitm()
# b.func()


# #Decorator -> calling the pre defined function
# # static method
# def my_bitm(fun):
#     def wrapper():
#         print("Before")
#         fun()
#         print("After")
#     return wrapper
# @my_bitm
# def greet():
#     print("hello")
# greet()


# # Class Method
# class Mrec:
#     Dept = "CSE"
#     def Dept_name(self,name):
#         print("Instance method",name)
    
#     @classmethod
#     def get_Dept(cls):
#         return cls.Dept
# m = Mrec()
# m.Dept_name("DS")
# print("Class method",Mrec.Dept)


 

        





