
# class Car:
#     # class variable
#     company = "Toyota"
#     count = 0
#     def __init__(self,brand,model,price):
#         # a = 10     instance variable
#         # self.company = company
#         self.brand = brand
#         self.model = model
#         self.price = price
        
    
#     def disp(self):
#         Car.count+=1
#         print("---------------------")
#         print(f"Company:{Car.company}\nBrand:{self.brand}\nModel:{self.model}\nPrice:{self.price}") 
        
# # Create object
# c1 = Car(input("Enter the Brand name:"),input("Enter the Model name:"),input("Enter the Price:"))
# c1.disp()
# c2 = Car(input("Enter the Brand name:"),input("Enter the Model name:"),input("Enter the Price:"))
# c2.disp()
# c3 = Car(input("Enter the Brand name:"),input("Enter the Model name:"),input("Enter the Price:"))
# c3.disp()
# print("Total Cars registered  is",Car.count)


# # q1 1 2 3 -> 1 2 4     q2 1 2 9 -> 1 3 0     q3 1 9 9 -> 2 0 0     
# class Solution(object):
#     def plusOne(self,digits):
#         for i in range(len(digits)-1,-1,-1):
#             if digits[i] == 9:
#                 digits[i] = 0
#             else:
#                 digits[i] += 1
#                 return digits
#         return [1] + digits
# obj = Solution()
# print(obj.plusOne([1,2,9]))

# Calculator program using methods 
# class Calculator:
#     sum = 0
#     def __init__(self,m,n,choice):
#         self.m = m
#         self.n = n
#         self.coice = choice
 
#     def sum(self): 
#         return self.m+self.n
#     def sub(self):
#         return self.m-self.n
#     def mul(self):
#         return self.m*self.n
#     def div(self):
#         return self.m/self.n


# c1 = Calculator(a = int(input("Enter the First number:")), 
#                 b = int(input("Enter the Second number:")),
#                 choice = input("Enter the operation (+,-,*,/):"))
# match c1.choice:
#     case "+":
#         print("The sum is",c1.sum())
#     case "-":
#         print("The sub is ",c1.sub())
#     case "*":
#         print("The mul is ",c1.mul())
#     case "/":
#         print("The div is ",c1.div())
#     case _:
#         print("Invalid choice")
    

# ------Factorial using classes and functions
def fact(n):
    if n == 0 | n == 1:
        return 1
    else:
       return  n*fact(n-1)
n = int(input("Enter the number:"))
for i in range(1,n+1):
    print(f"Factorial of {i} is:{fact(i)}")

 
 